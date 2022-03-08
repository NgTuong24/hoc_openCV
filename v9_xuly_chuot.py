import numpy as np
import cv2
# dir() tra ve cac thuoc tinh cua 1 doi tuong
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        st = str(x) + ', ' + str(y)
        cv2.putText(img, st, (x, y), font, 0.5, (255,255,0), 1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONUP:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        stBGR = str(blue) + ', ' + str(green) + ', '+ str(red)
        cv2.putText(img, stBGR, (x, y), font, 0.5, (0, 255, 255), 1)
        cv2.imshow('image', img)
# img = np.zeros((350,350,3), np.uint8)
img = cv2.imread('img.png')
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()