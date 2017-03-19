#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test.py

import numpy as np
import cv2

hsvWhiteLo = np.array([0, 8, 55], np.uint8)
hsvWhiteHi = np.array([180, 12, 65], np.uint8)

hsvRedLo = np.array([0, 43, 46], np.uint8)
hsvRedHi = np.array([5, 255, 255], np.uint8)

hsvOrangeLo = np.array([5, 43, 46], np.uint8)
hsvOrangeHi = np.array([12, 255, 255], np.uint8)

hsvYellowLo = np.array([22, 43, 46], np.uint8)
hsvYellowHi = np.array([38, 255, 255], np.uint8)

hsvGreenLo = np.array([40, 43, 46], np.uint8)
hsvGreenHi = np.array([90, 255, 255], np.uint8)

hsvBlueLo = np.array([100, 43, 46], np.uint8)
hsvBlueHi = np.array([124, 255, 255], np.uint8)

grid1_pt1 = (230, 150)
grid1_pt2 = (270, 190)

grid2_pt1 = (300, 150)
grid2_pt2 = (340, 190)

grid3_pt1 = (370, 150)
grid3_pt2 = (410, 190)

grid4_pt1 = (230, 220)
grid4_pt2 = (270, 260)

grid5_pt1 = (300, 220)
grid5_pt2 = (340, 260)

grid6_pt1 = (370, 220)
grid6_pt2 = (410, 260)

grid7_pt1 = (230, 290)
grid7_pt2 = (270, 330)

grid8_pt1 = (300, 290)
grid8_pt2 = (340, 330)

grid9_pt1 = (370, 290)
grid9_pt2 = (410, 330)

grid11_pt1 = (0, 0)
grid11_pt2 = (40, 40)

grid12_pt1 = (50, 0)
grid12_pt2 = (90, 40)

grid13_pt1 = (100, 0)
grid13_pt2 = (140, 40)

grid14_pt1 = (0, 0)
grid14_pt2 = (40, 40)

grid15_pt1 = (50, 0)
grid15_pt2 = (90, 40)

grid16_pt1 = (100, 0)
grid16_pt2 = (140, 40)

grid17_pt1 = (0, 0)
grid17_pt2 = (40, 40)

grid18_pt1 = (50, 0)
grid18_pt2 = (90, 40)

grid19_pt1 = (100, 0)
grid19_pt2 = (140, 40)

score = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
img = [
    np.zeros((40, 40), np.float32), np.zeros((40, 40), np.float32),
    np.zeros((40, 40), np.float32), np.zeros((40, 40), np.float32), np.zeros(
        (40, 40), np.float32), np.zeros((40, 40), np.float32), np.zeros(
            (40, 40), np.float32), np.zeros((40, 40), np.float32), np.zeros(
                (40, 40), np.float32)
]

color = [(0, 0, 255), (0, 130, 255), (0, 255, 255), (0, 255, 0), (255, 0, 0),
         (255, 255, 255)]

color_list = [
    hsvRedLo, hsvRedHi, hsvOrangeLo, hsvOrangeHi, hsvYellowLo, hsvYellowHi,
    hsvGreenLo, hsvGreenHi, hsvBlueLo, hsvBlueHi
]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.rectangle(frame, grid1_pt1, grid1_pt2, (255, 255, 255), 2)
    cv2.rectangle(frame, grid2_pt1, grid2_pt2, (255, 255, 255), 2)
    cv2.rectangle(frame, grid3_pt1, grid3_pt2, (255, 255, 255), 2)

    cv2.rectangle(frame, grid4_pt1, grid4_pt2, (255, 255, 255), 2)
    cv2.rectangle(frame, grid5_pt1, grid5_pt2, (255, 255, 255), 2)
    cv2.rectangle(frame, grid6_pt1, grid6_pt2, (255, 255, 255), 2)

    cv2.rectangle(frame, grid7_pt1, grid7_pt2, (255, 255, 255), 2)
    cv2.rectangle(frame, grid8_pt1, grid8_pt2, (255, 255, 255), 2)
    cv2.rectangle(frame, grid9_pt1, grid9_pt2, (255, 255, 255), 2)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for i in range(5):
        mask = cv2.inRange(hsv_frame, color_list[i * 2], color_list[i * 2 + 1])

        # Opening and Closing
        kernel = np.ones((5, 5), np.uint8)
        # opening remove noise
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # closing connect connected domains
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # Threshold
        ret, threshold = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
        # threshold = cv2.adaptiveThreshold(
        #     mask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)

        img[0] = threshold[grid1_pt1[1]:grid1_pt2[1], grid1_pt1[0]:grid1_pt2[
            0]]
        img[1] = threshold[grid2_pt1[1]:grid2_pt2[1], grid2_pt1[0]:grid2_pt2[
            0]]
        img[2] = threshold[grid3_pt1[1]:grid3_pt2[1], grid3_pt1[0]:grid3_pt2[
            0]]
        img[3] = threshold[grid4_pt1[1]:grid4_pt2[1], grid4_pt1[0]:grid4_pt2[
            0]]
        img[4] = threshold[grid5_pt1[1]:grid5_pt2[1], grid5_pt1[0]:grid5_pt2[
            0]]
        img[5] = threshold[grid6_pt1[1]:grid6_pt2[1], grid6_pt1[0]:grid6_pt2[
            0]]
        img[6] = threshold[grid7_pt1[1]:grid7_pt2[1], grid7_pt1[0]:grid7_pt2[
            0]]
        img[7] = threshold[grid8_pt1[1]:grid8_pt2[1], grid8_pt1[0]:grid8_pt2[
            0]]
        img[8] = threshold[grid9_pt1[1]:grid9_pt2[1], grid9_pt1[0]:grid9_pt2[
            0]]

        for j in range(9):
            score[j][i] = np.mean(img[j])

        # Find contours
        # ret, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE,
        # cv2.CHAIN_APPROX_SIMPLE)
        # for cnt in contours:
        #     x, y, w, h = cv2.boundingRect(cnt)
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    idx = np.argmax(np.array(score), axis=1)
    maxv = np.max(np.array(score), axis=1)
    for i in range(9):
        if (maxv[i] < 150):
            idx[i] = 5
    for j in range(6):
        if (idx[0] == j):
            cv2.rectangle(frame, grid1_pt1, grid1_pt2, color[j], -1)
    for j in range(6):
        if (idx[1] == j):
            cv2.rectangle(frame, grid2_pt1, grid2_pt2, color[j], -1)
    for j in range(6):
        if (idx[2] == j):
            cv2.rectangle(frame, grid3_pt1, grid3_pt2, color[j], -1)
    for j in range(6):
        if (idx[3] == j):
            cv2.rectangle(frame, grid4_pt1, grid4_pt2, color[j], -1)
    for j in range(6):
        if (idx[4] == j):
            cv2.rectangle(frame, grid5_pt1, grid5_pt2, color[j], -1)
    for j in range(6):
        if (idx[5] == j):
            cv2.rectangle(frame, grid6_pt1, grid6_pt2, color[j], -1)
    for j in range(6):
        if (idx[6] == j):
            cv2.rectangle(frame, grid7_pt1, grid7_pt2, color[j], -1)
    for j in range(6):
        if (idx[7] == j):
            cv2.rectangle(frame, grid8_pt1, grid8_pt2, color[j], -1)
    for j in range(6):
        if (idx[8] == j):
            cv2.rectangle(frame, grid9_pt1, grid9_pt2, color[j], -1)

    cv2.imshow('Original', frame)

    key = cv2.waitKey(10)
    if key == ord('o'):
        idx = idx.reshape((3, 3))
        print(idx)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
