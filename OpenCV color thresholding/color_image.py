import cv2
from cv2 import imread
from matplotlib import pyplot as plt
# ambil citra dari video

frame = cv2.imread("waf11.png", 1)
hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_blue = (70, 50, 50)
upper_blue = (120, 255, 255)
mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
img_new = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Yang harus dilakukan adalah beberapa langkah sebagai berikut:
### Cari contour dari mask ###
# gunakan metode cv2.findContours()
contours, hierarchy = cv2.findContours(mask,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

### Sort contour ###
# gunakan metode cv2.sorted()
# cv2.sorted()
# sorted = sorted(contours, key=cv2.contourArea, reverse=True)

### Cari 4 titik yang akan dihubungkan menjadi sebuah kotak ###
# gunakan metode cv2.boundingRect()
x, y, w, h = cv2.boundingRect(contours[0])

### Gambarlah kotak berdasarkan 4 titik tsb pada img_new ###
# gunakan metode cv2.rectangle()
# cv2.rectangle()
cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

### Tampilkan hasil ###
cv2.imshow("Video", frame)
# cv2.imshow("Video mask", mask)
cv2.waitKey()
cv2.destroyAllWindows()
