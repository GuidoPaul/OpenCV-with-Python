#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: canny-edge-detection-and-gradients.py

import cv2


def nothing(x):
    pass


cv2.namedWindow('canny')
cv2.createTrackbar('Low Thres', 'canny', 0, 255, nothing)
cv2.createTrackbar('High Thres', 'canny', 0, 255, nothing)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Laplacian
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    # Sobel
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    # Canny
    low_thres = cv2.getTrackbarPos('Low Thres', 'canny')
    high_thres = cv2.getTrackbarPos('High Thres', 'canny')
    canny = cv2.Canny(frame, low_thres, high_thres)

    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('canny', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
