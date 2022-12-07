import cv2 as cv

img = cv.imread('photos/sand.jpg')
cv.imshow('Demo', img)

cv.waitKey(0)
cv.destroyAllWindows