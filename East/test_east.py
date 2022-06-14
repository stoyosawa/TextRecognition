#!/usr/bin/env python
# 2022-06-04: EAST text detector

import itertools
import math
from sys import argv
import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

'''
Original implementation: https://docs.opencv.org/4.x/db/da4/samples_2dnn_2text_detection_8cpp-example.html
Many blogs discuss the EAST, however, they are all just copies (well, same here).
e.g, https://www.folio3.ai/blog/text-detection-by-using-opencv-and-east/

The original model accepts images with the sizes multiple of 32. It outputs the information about the images with the 1/4 of the input size.
'''

# Copied from my_util.py in Hough. I should re-organize the project structure ...
def solid_color(idx):
    ''' Generate solid colors from an integer. The function prepares 25 colors that come from the combinations of (0, 128, 255).'''
    lst = set(itertools.product((0, 128, 255), repeat=3))                    # Patterns of (0, 128, 255). 3 times to generate color tuples.
    lst = lst - set([(0, 0, 0), (255, 255, 255)])                            # Exclude pure white and black.
    idx = idx % (3 ** 3 - 2)                                                 # 3^3 -2 = 25 patterns
    return list(lst)[idx]


def aabb(x, y, geometry):
    '''
    cv2.dnn.Net.forward() returns the geometry information in AABB (Axis Aligned Bounding Box) format. See Section 3.2 of the original paper.
    The box is centered at the (x, y) of the resized image (1/4).
    First 4 numbers denote the distance from the center to the top, right, bottom and left segments of the bouding box. The 5th number is the rotation angle (in radian).
    This function returns the bounding box of the rectangle.
    '''
    top, right, bottom, left, theta = geometry

    # The center of the image. Note that the image is 1/4 of the original.
    offsetX, offsetY = (x * 4.0, y * 4.0)
    
    # height and width of the box
    h, w = (top + bottom, left + right)

    # angle - cos and sin.
    cos = math.cos(theta)
    sin = math.sin(theta)

    # Find the cordinates of the corners.
    endX = int(offsetX + (cos * right) + (sin * bottom))
    endY = int(offsetY - (sin * right) + (cos * bottom))
    startX = int(offsetX - w)
    startY = int(offsetY - h)

    return (startX, startY, endX, endY)



# The input image must be multiple of 32.
img = cv2.imread(argv[1])
h, w = [(d//32)*32 for d in img.shape[:2]]
img_resized = cv2.resize(img, (w, h))
print(f'Image resized from {img.shape} to {img_resized.shape}')

# Read the model. Function returns cv2.dnn.Net object.
net = cv2.dnn.readNet('Model/frozen_east_text_detection.pb')

# Create blob (4 dimensional) from the input.
blob = cv2.dnn.blobFromImage(
    img_resized,                                         # input
    mean=(123.68, 116,78, 103.94),                       # Subtract the average luminance of the training data. In order of RGB (not BGR).
    swapRB=True,                                         # Input BGR (OpenCV) image should be converted to RGB (Tensorflow).
    crop=False                                           # Cropped?
)
print(f'Blob shape: {blob.shape}')

# Create output layers
# See https://github.com/argman/EAST/issues/85 for the names of the layers.
outputLayers = []
outputLayers.append("feature_fusion/Conv_7/Sigmoid")
outputLayers.append("feature_fusion/concat_3")

# Add the layers
net.setInput(blob)

# The model returns a tuple with two elements.
# Image is 1/4 of the original.
# 
# scores is a (1, 1, h/4, w/4) matrix. It contains the probability (0 to 1) of the bounding box centered at (x, y) being the text area.
# e.g., to obtain the p of the rectangle at (x, y), get scores[0, 0, y, x].
#
# geometries is a (1, 5, h/4, w/4) matrix.
# The 5 elements of the geometries[1] are (y1, x1, y2, x2, θ) - This is the AABB bounding box. See function aabb above.
scores, geometries = net.forward(outputLayers)
print(f'Shapes: scores {scores.shape}, geometries {geometries.shape}')

# Extract the ones with score above a certain threshold.
rects = []
confidences = []
img_aabb = img_resized.copy()
color_idx = 0

for y in range(scores.shape[2]):
    for x in range(scores.shape[3]):
        p = scores[0, 0, y, x]
        if p > 0.9:
            pos = geometries[0, :, y, x]
            pos_string = [f'{d:.4f}' for d in pos]
            rect = aabb(x, y, geometries[0, :, y, x])
            # print(x*4, y*4, p, pos_string, rect)
            cv2.rectangle(img_aabb, (rect[0], rect[1]), (rect[2], rect[3]), solid_color(color_idx), thickness=1)
            color_idx += 1
            rects.append(rect)
            confidences.append(p)

print(f'{len(rects)} rectangles.')
cv2.imshow('Image', img_aabb)
cv2.waitKey()

# Use Non-Maxima Suppression (NMS) to integrate overlapping regions.
boxes = non_max_suppression(np.array(rects), probs=confidences)
print(f'Shape: boxes: {boxes.shape}')
img_boxes = img_resized.copy()

# Draw the bounding boxes.
for idx, box in enumerate(boxes):
    start = tuple(box[:2])
    end = tuple(box[2:])
    cv2.rectangle(img_boxes, start, end, solid_color(idx), thickness=2)

cv2.imshow('Image', img_boxes)
cv2.waitKey()
