import numpy as np
import time
from sklearn import datasets
from sklearn.metrics import classification_report,accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import pickle
import matplotlib.pyplot as plt

import cv2

class knn_predictor:
    def __init__(self,img):
        self.img = img

    def predict(self,lov):
        knn_model = pickle.load(open("knn.sav", 'rb'))
        cleanedimg = lov

        cleanedimg = cleanedimg.reshape(1, -1)
        s = np.sum(cleanedimg)
        if (s > 7 * 255):


            prediction = knn_model.predict(cleanedimg)[0]
            return prediction
    def Create_arr(self):
        final = self.img
        arr = np.zeros((9,9))
        for i in range(0, 9):
            for j in range(0, 9):
                lov = np.zeros((28, 28))
                t = np.zeros((28, 28))
                for l in range(0, 28):
                    for m in range(0, 28):
                        t[l][m] = final[28 * i + l][28 * j + m]
                        dim = (28 * 28, 1)
                        red = np.reshape(t, dim)

                        lov = np.reshape(red, (28, 28))
                        lov = lov.astype('uint8')
                arr[i][j] = self.predict(lov.copy())
        return arr




