






import numpy as np
import cv2 as cv
from picture_editing import VideoEditor


cap = cv.VideoCapture("Traffic IP Camera video (1).mp4")

bg_subs = cv.createBackgroundSubtractorMOG2()
history = 90
learning_rate = 1.0/history
while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break
    frame = VideoEditor.frame_edit(frame, 0.5)
    mask = bg_subs.apply(frame, learningRate=learning_rate)
    mask = VideoEditor.mask_edit(mask, 3, 1)
    out = frame.copy()
    # result = cv.bitwise_and(out, out, mask=mask)
    # cv.imshow('res', mask)
    VideoEditor().find_ctr(mask, out)
    cv.imshow("input", out)
    c = cv.waitKey(10)
    if c == 27:
        break
cap.release()
cv.destroyAllWindows()