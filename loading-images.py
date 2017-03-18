#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: intro.py

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# cv2.imshow('Lenna', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.plot([50, 100], [80, 200], 'c', linewidth=2)
plt.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=2)
plt.show()

# plt.savefig('images/Lenna-gray.png')
cv2.imwrite('images/Lenna-gray.png', img)
