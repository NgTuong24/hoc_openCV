import numpy as np
import cv2
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        st = str(x) + ', ' + str(y)
        cv2.putText(img, st, (x, y), font, 0.5, (255,255,0), 1)
        cv2.imshow('image', img)

img = cv2.imread('messi5.png')
img2 = cv2.imread('opencv-logo.png')

print(img.shape) # returns a tuple of number of rowa, columns, and  channels
print(img.size)  # returns total number of pixels is accessed
print(img.dtype) # returns Image datatype is obtained
b, g, r = cv2.split(img)
# print(cv2.split(img))
img = cv2.merge((b, g, r))

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball


img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .9, img2, .1, 0)
cv2.imshow('image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()