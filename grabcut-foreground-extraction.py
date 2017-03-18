#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: grabcut-foreground-extraction.py

import numpy as np
import cv2

img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
