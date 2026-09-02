import cv2 as cv

image = cv.imread('Basics/assets/maxresdefault.jpg')
cv.imshow('Image', image)
cv.waitKey(0)
cv.destroyAllWindows()

