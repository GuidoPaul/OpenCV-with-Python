#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: blurring-and-smoothing.py

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150, 150, 50])
    upper_red = np.array([180, 255, 150])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Simple Smoothing
    kernel = np.ones((5, 5), np.float32) / 25
    smoothed = cv2.filter2D(res, -1, kernel)

    # Gaussian Blur
    blur = cv2.GaussianBlur(res, (15, 15), 0)
    # Median Blur
    median = cv2.medianBlur(res, 15)
    # Bilateral Blur
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('Gaussian Blurring', blur)
    cv2.imshow('Median Blur', median)
    cv2.imshow('Bilateral', bilateral)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
