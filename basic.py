import cv2 as cv
import numpy as np

img = cv.imread('Photos/img-3.png')
cv.imshow('Cat', img)

cv.waitKey(0)