#####
#
# файл с методами для работы с изображением
#
#####
import cv2 as cv
import numpy as np

class VideoEditor:
    @staticmethod
    def frame_edit(frame, scale):
        frame = cv.resize(frame, None, fx=scale, interpolation=cv.INTER_AREA)
        return frame

    @staticmethod
    def mask_edit(frame, kernel, iterations):
        kernel = np.ones((kernel, kernel), np.uint8)
        opening = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
        # dilation = cv.dilate(frame, kernel, iterations=iterations)
        return opening
    @staticmethod
    def find_ctr(frame):
        ret, thresh = cv.threshold(frame, 170, 255, 0)
        im2, contours, hierarchy = cv.findContours(
            thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE
        )
        cv.drawContours(res, contours, )