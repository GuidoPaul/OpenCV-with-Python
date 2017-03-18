#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: drawing-and-writing-on-image.py

import numpy as np
import cv2

img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (200, 200), (0, 0, 255), 5)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.circle(img, (30, 200), 40, (255, 0, 0), -1)

pts = np.array([[5, 5], [100, 100], [80, 300], [90, 60]], np.int32)
cv2.polylines(img, [pts], True, (255, 255, 0), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tus!', (0, 130), font, 1, (255, 255, 255), 5,
            cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
