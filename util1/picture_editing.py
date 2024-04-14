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
    def find_ctr_centers(frame, res):
        ret, thresh = cv.threshold(frame, 170, 255, 0)
        contours, hierarchy = cv.findContours(
            thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE
        )
        out = []
        for c in contours:
            M = cv.moments(c)
            if M['m00'] > 1000:
               cX = int(M['m10'] / M['m00'])
               cY = int(M['m01'] / M['m00'])
               out.append((cX, cY))
               cv.circle(res, (cX,cY), 10, (0, 255, 0), -1)
        cv.drawContours(res, contours, -1, (0, 255, 0), 3)

    @staticmethod
    def interface(frame, label):
        string_out = f'N cars: {label}'
        cv.rectangle(frame, (277, 70), (640, 110), (255, 0, 0), 3)
        cv.putText(frame, label, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1,(20, 20, 255), 2, cv.LINE_AA)

        # moments = cv.moments(frame)
        # dM01 = moments['m01']
        # dM10 = moments['m10']
        # darea = moments['m00']
        # if darea > 10:
        #    x = int(dM10 / darea)
        #    y = int(dM10 / darea)
        #    cv.circle(res, (x,y), 10, (0, 255, 0), -1)

    @staticmethod
    def car_check(arr_of_centers):
        XMIN = 340
        XMAX = 490
        YMIN = 400
        YMAX = 400
        k = 0
        for center in arr_of_centers:
            x, y = center
            if (XMIN <= x <= XMAX) and (YMIN <= y <= YMAX):
                k += 1
        return k
