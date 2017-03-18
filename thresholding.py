#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: thresholding.py

import cv2

img = cv2.imread('bookpage.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# simple threshold
ret, threshold = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
ret, threshold2 = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY, 115, 1)
ret, otsu = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('threshold3', gaus)
cv2.imshow('threshold4', otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
