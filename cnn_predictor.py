import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import pickle


class predictor:
    def __init__(self,img):
        self.img = img

    def predict(self,lov):
        model = tf.keras.models.load_model("cnn.hdf5")
        cleanedimg = lov
        temp = lov.reshape(1, -1)
        s = np.sum(temp)

        if (s > 7 * 255):

            lis = [cleanedimg]

            lis = np.resize(lis, (28, 28))
            #print(np.shape(cleanedimg))


            lis = np.reshape(lis, (1, 28, 28, 1))
            lis = lis.astype('float32')
            idx = None
            pred = model.predict_classes(lis)
            ans = (pred[0])
            #print(pred[0])
            #plt.imshow(cleanedimg, cmap='gray', vmin=0, vmax=255)
            #plt.show()
        else:
            ans = 0
        return ans



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
