import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255,255,255), -1)
img2 = cv2.imread("image_1.png")
img2 = cv2.resize(img2, (500, 250))

# bitAND = cv2.bitwise_and(img1, img2)
# bitOR = cv2.bitwise_or(img1, img2)
# bitXOR = cv2.bitwise_xor(img1, img2)

# dao nguoc
bitNOT = cv2.bitwise_not(img1)
bitNOT2 = cv2.bitwise_not(img2)
'''
XOR
0 0 > 0
0 1 > 1
1 0 > 1
1 1 > 0
'''
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
# cv2.imshow("bit_and", bitAND)
# cv2.imshow("bit_or", bitOR)
# cv2.imshow("bit_xor", bitXOR)
cv2.imshow("bit_not_1", bitNOT)
cv2.imshow("bit_not_2", bitNOT2)
cv2.waitKey(0)
cv2.destroyAllWindows()