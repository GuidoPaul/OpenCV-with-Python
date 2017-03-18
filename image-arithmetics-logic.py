#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: image-arithmetics-logic.py

import cv2

# 500 x 250
img1 = cv2.imread('images/3D-Matplotlib.png')
img2 = cv2.imread('images/mainsvmimage.png')

# simple addition
add1 = img1 + img2
# opencv's add method
# (155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255)
add2 = cv2.add(img1, img2)
# opencv's addWeighted method
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('add1', add1)
cv2.imshow('add2', add2)
cv2.imshow('weighted', weighted)
cv2.waitKey(0)

# -------------------------------------------------------

# Load two images
dota = cv2.imread('images/dota.jpg')
logo = cv2.imread('images/dota_logo.jpg')

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = logo.shape
roi = dota[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask
logo2gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(logo2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
dota_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
dota_fg = cv2.bitwise_and(logo, logo, mask=mask)

dst = cv2.add(dota_bg, dota_fg)
dota[0:rows, 0:cols] = dst

cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('dota_bg', dota_bg)
cv2.imshow('dota_fg', dota_fg)
cv2.imshow('dst', dst)
cv2.imshow('dota with logo', dota)
cv2.waitKey(0)

cv2.destroyAllWindows()
