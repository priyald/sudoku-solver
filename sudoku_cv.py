import cv2
import tensorflow as tf
import numpy as np
import utils as ut

height = 350
width = 350

sudoku = ut.getImagepath()
sudoku = cv2.resize(sudoku, height, width)
answer = np.zeros((height, width, 3))


#pre-process the image
#turn it to grayscale, add gaussian blur, apply adaptive threshold
sudoku = cv2.cvtColor(sudoku, cv2.COLOR_BGR2GRAY)
sudoku = cv2.GaussianBlur(sudoku, (5,5), 1)
sudoku = cv2.adaptiveThreshold(sudoku, 255, 1, 1, 11, 2)

#find all contours of the image
sudoku_contours = cv2.findContours(sudoku, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
sudoku_big_contour = ut.biggestContour(sudoku_contours)
