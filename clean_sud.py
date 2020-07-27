import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import operator
import PIL
from PIL import Image

class sudoku:
    def __init__(self,image):
        self.img = image

    def obtain_dig(self,img):
        '''
        return a list containing the coords of the ends of the squares
        of the digit
        '''
        digits = []
        h, w = np.shape(img[:])
        dig_h = int(h / 9)
        dig_w = int(w / 9)

        for j in range(0, 9):
            for i in range(0, 9):
                tl = (i * dig_h, j * dig_w)
                br = (i * dig_h + dig_h, j * dig_w + dig_w)
                points = (tl, br)
                digits.append(points)
        return digits,dig_h

    def processing(self,dig_img):
        maxi = 0
        seed = (None, None)
        side, side = np.shape(dig_img[:])
        margin = int(side / 6)
        corner = [margin, side - margin, margin, side - margin]
        for y in range(corner[0], corner[1]):
            row = dig_img[y]
            for x in range(corner[2], corner[3]):
                if row[x] >= 128:
                    area = cv2.floodFill(dig_img, None, (x, y), 64)[0]
                    if (area > maxi):
                        seed = (x, y)
                        maxi = area

        for y in range(0, side):
            row = dig_img[y]
            for x in range(0, side):
                if (row[x] >= 128):
                    cv2.floodFill(dig_img, None, (x, y), 64)

        if maxi > 0:
            cv2.floodFill(dig_img, None, seed, 255)

        top, bottom, left, right = side, 0, side, 0

        for y in range(0, side):
            row = dig_img[y]
            for x in range(0, side):

                if (row[x] > 0 and row[x] < 250):
                    cv2.floodFill(dig_img, None, (x, y), 0)

                # Find the bounding parameters
                if row[x] == 255:
                    top = y if y < top else top
                    bottom = y if y > bottom else bottom
                    left = x if x < left else left
                    right = x if x > right else right

        ends = [[top, left], [bottom, right]]

        return dig_img,ends

    def cut_img(self,img, ends):
        copy = img[ends[0][0]: ends[1][0], ends[0][1]: ends[1][1]]
        return copy

    def scale_and_centre(self,img, size, margin=0, background=0):
        """Scales and centres an image onto a new background square."""
        h, w = img.shape[:2]

        def centre_pad(length):
            """Handles centering for a given length that may be odd or even."""
            if length % 2 == 0:
                side1 = int((size - length) / 2)
                side2 = side1
            else:
                side1 = int((size - length) / 2)
                side2 = side1 + 1
            return side1, side2

        def scale(r, x):
            return int(r * x)

        if h > w:
            t_pad = int(margin / 2)
            b_pad = t_pad
            ratio = (size - margin) / h
            w, h = scale(ratio, w), scale(ratio, h)
            l_pad, r_pad = centre_pad(w)
        else:
            l_pad = int(margin / 2)
            r_pad = l_pad
            ratio = (size - margin) / w
            w, h = scale(ratio, w), scale(ratio, h)
            t_pad, b_pad = centre_pad(h)

        img = cv2.resize(img, (w, h))
        img = cv2.copyMakeBorder(img, t_pad, b_pad, l_pad, r_pad, cv2.BORDER_CONSTANT, None, background)
        return cv2.resize(img, (size, size))

    def cleaned_sud(self):
        resized = self.img
        digits, side = self.obtain_dig(resized)
        dig_img = np.zeros((side, side))
        sud = resized.copy()

        for j in range(0, 9):
            for i in range(0, 9):
                index = i + (9 * j)
                (tl, br) = digits[index]
                dig_img = resized[tl[0]:br[0], tl[1]:br[1]]
                dig_img, ends = self.processing(dig_img)

                hei = ends[1][0] - ends[0][0]
                wid = ends[1][1] - ends[0][1]

                if (hei * wid < 1600 and hei * wid > 20):
                    img_bb = self.cut_img(dig_img, ends)
                    last = self.scale_and_centre(img_bb, side, margin=4, background=0)
                else:
                    last = np.zeros((40, 40))
                sud[40 * i:40 * (i + 1), 40 * j:40 * (j + 1)] = last

        return resized,sud
    def resize(self):
        dim = (28*9,28*9)
        _,sud = self.cleaned_sud()
        final = cv2.resize(sud,dim)
        return final









