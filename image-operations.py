#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: image-operations.py

import cv2

img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

# reference certain characteristics of our image
print('image shape:', img.shape)
print('image size:', img.size)
print('image dtype:', img.dtype)

# reference and change a pixel
img[55, 55] = [255, 255, 255]
px = img[55, 55]
print(px)

# reference an ROI
img[300:350, 300:350] = [255, 255, 255]

# copy and paste operations
lenna_face = img[150:400, 200:350]
img[0:250, 0:150] = lenna_face

cv2.imshow('image', img)
cv2.waitKey(0)
