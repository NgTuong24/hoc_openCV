import cv2
import numpy as np
#img = cv2.imread('img.png')
img = np.zeros([512, 512, 3], np.uint8)

# lay kich co anh
h, w, d= img.shape
print(h, w, d)


img = cv2.line(img, (0,0), (255,255), (0,0,  255), 10)
img = cv2.arrowedLine(img, (0,255), (255,255), (0,255, 0), 10)
img = cv2.rectangle(img, (0, 0), (300, 300), (0, 0, 255), 10)
#thickness = -1 ->fill
img = cv2.circle(img, (255, 255), 200, (250, 0, 0), 10)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'hello', (10,400), font, 4, (255,255,255), 10, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()