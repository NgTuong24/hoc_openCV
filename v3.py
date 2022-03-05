import cv2

img = cv2.imread('img.png', 0)
# print(img)
cv2.imshow('image', img)
cv2.imwrite('img_copy.png', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('img_copy.png', img)
    cv2.destroyAllWindows()
