import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import operator
import PIL
from PIL import Image


class Image:
############################################
# Processing of img.
    def __init__(self,path):
        self.path = path

    def img(self):
        img = cv2.imread(self.path, 0)
        return img


    def pre_process(self):
# This returns the thresholded img
        #Steps :
        # 1. Blurring to remove noise in img
        # 2. Thresholding the img to either 0
        img = self.img()
        puzzle = img
        out_box = np.zeros((np.size(puzzle)), np.uint8)
        dst = cv2.GaussianBlur(puzzle, (9, 9), 0)
        kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
        kernel2 = np.ones((3, 3), np.int8)
        out_box = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        out_box = cv2.bitwise_not(out_box)
        real = out_box.copy()
        return real

    def make_video(self):

        image_folder = 'flood'
        video_name = 'video.avi'

        images = [img for img in os.listdir(image_folder) if img.endswith(".jpeg")]
        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        length = len(images)
        video = cv2.VideoWriter(video_name, 0, int(length / 20), (width, height))

        for i in range(1, length + 1):
            image = str(i) + ".jpeg"
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()
        print('Video generated !!')


    def flood_fill(self,video = False):
        '''
        Flood filling is done to obtain the largest blob.
        #Process :
        #1. Flood fill everything with '64' brightness. Meanwhile
        find the largest flood-filled area and its seed point.
        #2. Then reflood the largest blob with 255.
        #3. Reset every pixel left with 64 to zero.

        VIDEO is to generate a video of of the action of floodfill algo.
        '''

        out_box = self.pre_process()

        maxi = -1
        maxpt = (None,None)

        height, width = np.shape(out_box)
        m = 0
        for y in range(height):
            row = out_box[y]
            for x in range(width):
                if row[x] >= 128:
                    area = cv2.floodFill(out_box, None, (x, y), 64)[0]
                    if(video == True):
                        m = m + 1
                        title = "flood/" + str(m) + ".jpeg"
                        cv2.imwrite(title, out_box)
                        # print(title + " under  progress ")
                    if area > maxi:
                        maxpt = (x, y)
                        maxi = area

        final = cv2.floodFill(out_box, None, maxpt, 256)
        if (video == True):
            m = m + 1
            title = "flood/" + str(m) + ".jpeg"
            cv2.imwrite(title, out_box)

        for y in range(height):
            row = out_box[y]
            # plt.imshow(out_box,cmap='gray', vmin=0, vmax=255)
            # print(row)
            for x in range(width):
                # print(row)
                if row[x] == 64:
                    cv2.floodFill(out_box, None, (x, y), 0)

        if (video == True):
            m = m + 1
            title = "flood/" + str(m) + ".jpeg"
            cv2.imwrite(title, out_box)
            self.make_video()

        return out_box

    def erode(self):
        '''
        Mainly to get better contour edges.
        '''
        out_box = self.flood_fill()
        kernel = np.ones((2, 2), np.uint8)
        img_dil = cv2.erode(out_box, kernel, iterations=1)
        return img_dil

    def find_contours(self):
        copy = self.erode()
        contours, h = cv2.findContours(copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        large = contours[0]
        result_img = cv2.cvtColor(self.pre_process(), cv2.COLOR_GRAY2RGB)
        cv2.drawContours(result_img, contours, 0, (0, 230, 255), 6)

        return result_img,large

    def warped_img(self):

        def dist(a, b):
            return (np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2))

        _,polygon = self.find_contours()

        bottom_right, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
        top_left, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
        bottom_left, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
        top_right, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in polygon]), key=operator.itemgetter(1))

        rect = np.zeros((4, 2), dtype="float32")
        rect[0] = polygon[top_left][0]
        rect[1] = polygon[top_right][0]
        rect[2] = polygon[bottom_right][0]
        rect[3] = polygon[bottom_left][0]

        (tl, tr, br, bl) = rect
        w_a = dist(tl, tr)
        w_b = dist(bl, br)

        maxWidth = int(max(w_a, w_b))

        h_a = dist(tl, bl)
        h_b = dist(tr, br)
        maxHeight = int(max(h_a, h_b))

        dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], dtype="float32")

        M = cv2.getPerspectiveTransform(rect, dst)
        warp = cv2.warpPerspective(self.pre_process(), M, (maxWidth, maxHeight))

        return warp

    def resize(self):
        dim = (40 * 9, 40 * 9)
        resized = cv2.resize(self.warped_img(), dim)
        return resized



##############################################
'''
cv2.imshow('STAGE-101', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


'''
path = Image('sudoku_2.jpeg')
STAGE_101 = path.img()
STAGE_102 = path.pre_process()

STAGE_103 = path.flood_fill()
STAGE_104 = path.erode()
STAGE_105,contour = path.find_contours()
STAGE_106 = path.warped_img()
STAGE_107 = path.resize()





cv2.imshow('STAGE-103', STAGE_107)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#############################################