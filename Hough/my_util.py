#!/usr/bin/env python
# 2022-06-03: Utlities functions for text region detections.

import itertools
import math
from sys import argv
import cv2
import numpy as np


def rad2deg(rad):
    ''' Radian to deg. '''
    return rad * 180 / math.pi


def deg2rad(deg):
    ''' Degree to radian. '''
    return deg * math.pi / 180


def solid_color(idx):
    ''' Generate solid colors from an integer. The function prepares 25 colors that come from the combinations of (0, 128, 255).'''
    lst = set(itertools.product((0, 128, 255), repeat=3))                    # Patterns of (0, 128, 255). 3 times to generate color tuples.
    lst = lst - set([(0, 0, 0), (255, 255, 255)])                            # Exclude pure white and black.
    idx = idx % (3 ** 3 - 2)                                                 # 3^3 -2 = 25 patterns
    return list(lst)[idx]


def make_blob(img, closing_iterations=1):
    '''
    Create a blob image from a scanned text.
    Returns a binarized gray-scale (text area white - foreground).
    '''
    # Convert to gray    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # OpenCV's samples/cpp/squares.cpp (detection of squares) uses pyramid (I presume for noise reduction). I don't know it helps, though.
    gray = cv2.pyrDown(gray)                             # Halve by default
    gray = cv2.pyrUp(gray)                               # Double by default

    # Binarize (0, 255)
    _, edges = cv2.threshold(                            # Turn into binary image
        gray,                                            # Input grayscalae image
        128,                                             # Threhold. Ignored because OTSU is used.
        255,                                             # Maxval
        cv2.THRESH_BINARY_INV |  cv2.THRESH_OTSU         # Inverted to make the text area white (fg)
    )

    # Closing (dilate-erode) morph. (Empirically, for 13x13 kernel) once is enough.
    kernel = np.ones((13, 13), np.uint8)
    morphed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=closing_iterations)

    # Contour. squares.cpp says Canny helps detecting squares with gradient shades.
    canny = cv2.Canny(morphed, 50, 100)

    return canny


def draw_axes(img, color=(255, 255, 0)):
    '''Draw horizontal (x) and vertical (y) axes. The center of the axes is at the center of the image.'''
    wh = tuple(reversed(img.shape[:2]))                  # (w, h). Not (rows, cols).
    center = [d//2for d in wh]

    cv2.line(img, (center[0], 0), (center[0], wh[1]-1), color=color, thickness=1, lineType=cv2.LINE_4)
    cv2.line(img, (0, center[1]), (wh[0]-1, center[1]), color=color, thickness=1, lineType=cv2.LINE_4)
    cv2.circle(img, center, radius=3, color=color, thickness=cv2.FILLED)

    return None


def rotate(img, angle):
    ''' Rotate the image by the angle (radian) around the center of the image. Note that + for θ is "counter-clockwise". '''
    angle = rad2deg(angle)
    wh = tuple(reversed(img.shape[:2]))                  # (w, h). Not (rows, cols).
    center = [d//2for d in wh]
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0) # angle in degree (counter-clockwise)
    rotated = cv2.warpAffine(img, matrix, wh)

    return rotated



if __name__ == '__main__':
    img = cv2.imread(argv[1])

    # Test blob
    blob = make_blob(img)
    cv2.imshow('Blob', blob)

    # Test rotate.
    rotated = rotate(blob, math.pi/6)
    cv2.imshow('Rotated (clock-wise)', rotated)

    cv2.waitKey()
