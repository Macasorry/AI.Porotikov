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
        frame = cv.resize(frame, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA)
        return frame
    @staticmethod
    def filter_img(frame, kernel):
        kernel = np.ones((kernel, kernel), np.uint8)
        opening = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
        return opening
    @staticmethod
    def mask_edit(frame, kernel, iterations):
        kernel = np.ones((kernel, kernel), np.uint8)
        # opening = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
        dilation = cv.dilate(frame, kernel, iterations=iterations)
        return dilation
    @staticmethod
    def find_ctr(frame, res):
        ret, thresh = cv.threshold(frame, 170, 255, 0)
        contours, hierarchy = cv.findContours(
            thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE
        )

        for c in contours:
            M = cv.moments(c)
            if M['m00'] > 2000:
               cX = int(M['m10'] / M['m00'])
               cY = int(M['m01'] / M['m00'])


        moments = cv.moments(frame)
        dM01 = moments['m01']
        dM10 = moments['m10']
        darea = moments['m00']
        if darea > 10:
           x = int(dM10 / darea)
           y = int(dM10 / darea)
           cv.circle(res, (x,y), 10, (0, 255, 0), -1)
        cv.drawContours(res, contours, -1, (0, 255, 0), 3)