#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: MOG-background-reduction.py

import cv2

cap = cv2.VideoCapture('videos/people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
