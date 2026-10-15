import cv2 as cv

image = cv.imread('Basics/assets/maxresdefault.jpg')
cv.imshow('Image', image)
cv.waitKey(0)
cv.destroyAllWindows()

width = 800
hight = 400

image = cv.resize(image,(width, hight))
cv.imshow('Resized', image)
cv.waitKey(0)
cv.destroyAllWindows()

image = cv.flip(image,1)
cv.imshow('flip', image)
cv.waitKey(0)
cv.destroyAllWindows()

image = cv.rotate(image,cv.ROTATE_90_COUNTERCLOCKWISE)
cv.imshow('Rotate', image)
cv.waitKey(0)
cv.destroyAllWindows()

image = cv.GaussianBlur(image,(3,3),0)
cv.imshow('Blur', image)
cv.waitKey(0)
cv.destroyAllWindows()
