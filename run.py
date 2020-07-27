
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import operator
import PIL
from PIL import Image

from process import Image
from clean_sud import sudoku
from cnn_predictor import predictor
from knn import knn_predictor
from GUI import UI

path = Image('test_images/sudoku_3.jpeg')
STAGE_101 = path.img()
cv2.imwrite('STAGES/STAGE_101.jpg',STAGE_101 )
'''
cv2.imshow('STAGE-101', STAGE_101)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''



STAGE_102 = path.pre_process()
cv2.imwrite('STAGES/STAGE_102.jpg',STAGE_102 )
#cv2.waitKey(0)
cv2.destroyAllWindows()
STAGE_103 = path.flood_fill(video=False)
cv2.imwrite('STAGES/STAGE_103.jpeg',STAGE_103 )
STAGE_104 = path.erode()
cv2.imwrite('STAGES/STAGE_104.jpg',STAGE_104)
STAGE_105,contour = path.find_contours()
cv2.imwrite('STAGES/STAGE_105.jpg',STAGE_105 )
STAGE_106 = path.warped_img()
cv2.imwrite('STAGES/STAGE_106.jpg',STAGE_106 )
STAGE_107 = path.resize()
cv2.imwrite('STAGES/STAGE_107.jpg',STAGE_107 )
print('done')
plt.imshow(STAGE_106,cmap='gray', vmin=0, vmax=255)

'''
Sud = sudoku(STAGE_107.copy())
STAGE_201,STAGE_202 = Sud.cleaned_sud()
STAGE_203 = Sud.resize()

model = predictor(STAGE_203.copy())
array = model.Create_arr()


maze = array.astype(np.uint8)



SUSO = UI(maze)
SUSO.createGUI()
'''





