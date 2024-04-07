import numpy as np
import cv2 as cv
from util.picture_editing import VideoEditor



cap = cv.VideoCapture("Traffic IP Camera video.mp4")

bg_subs = cv.createBackgroundSubtractorMOG2()
history = 90
learning_rate = 1.0/history
while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break
    frame = VideoEditor.frame_edit(frame, 1)
    mask = bg_subs.apply(frame, learningRate=learning_rate)
    out = frame.copy()
    # result = cv.bitwise_and(out, out, mask=mask)
    # cv.imshow('res', mask)

    ret, thresh1 = cv.threshold(mask, 50, 255, cv.THRESH_BINARY)
    filter_img = VideoEditor.filter_img(thresh1, 5)
    edited = VideoEditor.mask_edit(filter_img, 3, 3)
    # cv.imshow('1', mask)
    # cv.imshow('2', thresh1)
    # cv.imshow('3', edited)

    VideoEditor().find_ctr(edited, out)
    cv.imshow("input", out)
    c = cv.waitKey(10)
    if c == 27:
        break
cap.release()
cv.destroyAllWindows()