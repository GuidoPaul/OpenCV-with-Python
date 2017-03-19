#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: feature-matching.py

import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('images/opencv-feature-matching-template.jpg',
                  cv2.IMREAD_COLOR)
img2 = cv2.imread('images/opencv-feature-matching-image.jpg', cv2.IMREAD_COLOR)

# Create detector
orb = cv2.ORB_create()

# Find the key points and their descriptors with the orb detector
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Create matches of the descriptors, and sort them based on their distances
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Drawn the first 10 matches
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

b, g, r = cv2.split(img3)
img4 = cv2.merge([r, g, b])

plt.imshow(img4)
plt.show()
