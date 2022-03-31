import cv2 as cv
import numpy as np

img = cv.imread("gradient.png", 0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
#duy tri pixel 127 not change từ pixel127
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
# pixel <127 >> zero:black , > 127 giữ nguyên
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)
cv.waitKey(0)
cv.destroyAllWindows()
'''
THRESH_BINARY: Có thể dịch là ngưỡng nhị phân. Ý nghĩa y hệt những gì mình đề cập ở trên.

THRESH_BINARY_INV: Ngưỡng nhị phân đảo ngược. Có thể hiểu là nó sẽ đảo ngược lại kết quả của THRESH_BINARY.

THRESH_TRUNC: Những giá trị điểm ảnh bé hơn ngưỡng sẽ giữ nguyên giá trị, những điểm ảnh lớn hơn hoặc ngưỡng sẽ được gán lại là maxvalue.

THRESH_TOZERO: Những điểm ảnh bé hơn ngưỡng sẽ bị gán thành 0, những điểm còn lại giữ nguyên.

THRESH_TOZERO_INV: Những điểm ảnh nhỏ hơn giá trị ngưỡng sẽ được giữ nguyên, những điểm ảnh còn lại sẽ bị gán thành 0.

THRESH_MASK: Ở bạn opencv4, hầu như không được xài.

THRESH_OTSU: Sử dụng thuật toán Otsu để xác định giá trị ngưỡng.

THRESH_TRIANGLE: Sử dụng thuật toán Triangle để xác định giá trị ngưỡng.
'''