#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: template-matching.py

import numpy as np
import cv2

img_bgr = cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('opencv-template-for-matching.jpg', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where(res >= threshold)

for ptw, pth in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, (ptw, pth), (ptw + w, pth + h), (0, 0, 255), 2)

cv2.imshow('image', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
