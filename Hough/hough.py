#!/usr/bin/env python
# 2022-06-02

import math
import sys
import cv2
import numpy as np
from my_util import rad2deg, make_blob, draw_axes, rotate

'''
Detect the orientation of a scanned document using the Hough Line Transformation, and straighten it.
'''

def hough(img):
    hough_lines = cv2.HoughLinesP(                       # The function returns a list of list of tuple[ [(x1, y1, x2, y2), .... ] ]
        img,                                             # Accepts a 8-bit, single channel binary image
        rho=1,                                           # Distance resolution (1 pix)
        theta=np.pi/180,                                 # Angle resolution (1 deg)
        threshold=50,                                    # a number of votes (intersections)
        minLineLength=20,
        maxLineGap=5
    )

    # Assume the text flows horizontally: Vertical and diagonal lines are ignored.
    lines = []
    threshold = 20 * math.pi / 180                       # Assume the horizontal line is less than 20 deg.
    for line in hough_lines:
        x1, y1, x2, y2 = line[0]

        # Calculate angle
        if x2 - x1 == 0:                                 # Vertical
            theta = math.pi / 2
        else:
            theta = math.atan((y2 - y1) / (x2 - x1))

        if math.fabs(theta) < threshold:
            lines.append((*line[0], theta))

    return lines                                         # Retruns a list of [(x1, y1, x2, y2, theta), ....]


def draw_lines(img, lines):
    for line in lines:
        x1, y1, x2, y2, theta = line
        if theta > 0:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        cv2.line(img, (x1, y1), (x2, y2), color, 1)

    return img



def get_tilt(lines):
    '''
    The angle (radian) is calculated intentionally based on the math cordinate (Y upwards).
    By rotating this angle, it adjusts the angle from the hough funciton.
    '''
    thetas = [elem[4] for elem in lines]
    mean = np.mean(thetas)
    std = np.std(thetas)
    return (mean, std)



if __name__ == '__main__':
    file = sys.argv[1]                                   # Specify your image file from the command line
    orig = cv2.imread(file)
    cv2.imshow('orig', orig)

    blob = make_blob(orig)                               # Gray > threshold > morph > canny
    cv2.imshow('blob', blob)
    lines = hough(blob)
    mean, stdev = get_tilt(lines)
    print(f'Found {len(lines)} horizontal lines. {rad2deg(mean):.3f} ± {rad2deg(stdev):.3f} deg')

    with_lines = draw_lines(orig, lines)
    rotated = rotate(with_lines, mean)
    cv2.imshow('rotated', rotated)

    cv2.waitKey()
    # End
