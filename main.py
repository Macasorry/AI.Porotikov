import numpy as np
import cv2 as cv
from util.picture_editing import VideoEditor


cap = cv.VideoCapture("videoframe.mp4")

bg_subs = cv.createBackgroundSubtractorMOG2()
history = 300
learning_rate = 1.0/history
while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break
    frame = VideoEditor.frame_edit(frame, 1)
    mask = bg_subs.apply(frame, learningRate=learning_rate)
    out = frame.copy()
    out_frame = frame.copy()
    # result = cv.bitwise_and(out, out, mask=mask)
    # cv.imshow('res', mask)

    ret, thresh1 = cv.threshold(mask, 50, 255, cv.THRESH_BINARY)
    filter_img = VideoEditor.filter_img(thresh1, 5)
    edited = VideoEditor.mask_edit(filter_img, 3, 3)
    # cv.imshow('1', mask)
    # cv.imshow('2', thresh1)
    # cv.imshow('3', edited)
    arr_count = VideoEditor().find_ctr_centers(edited, out)
    count = VideoEditor().car_check(arr_count)

    if arr_count_old == 1 and count == 0:
        S += 1
    arr_count_old = count
    VideoEditor().interface(out, S)
    cv.imshow("input", out_frame)
    c = cv.waitKey(10)
    if c == 27:
        break
cap.release()
cv.destroyAllWindows()