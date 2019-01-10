import cv2
import numpy as np

img = cv2.imread('tiger.jpg',cv2.IMREAD_COLOR)

px = img[55,55]
img[55,55] = [255,255,255]
px = img[55,55]
print(px)

px = img[100:150,100:150]
print(px)
img[100:150,100:150] = [255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)

watch_face = img[100:150,150:200]
img[0:50,0:50] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
