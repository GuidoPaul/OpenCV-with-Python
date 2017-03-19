#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: grabcut-foreground-extraction.py

import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('images/opencv-python-foreground-extraction-tutorial.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (161, 79, 150, 150)  # x, y, w, h

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = img * mask2[:, :, np.newaxis]

# matplotlib rgb, opencv bgr
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])

plt.imshow(img2)
plt.colorbar()
plt.show()
