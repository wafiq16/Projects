import cv2
# import library opencv
import numpy as np
# import library numpy

# resolusi video
im_width = 640
im_height = 480

# buka file video
cap = cv2.VideoCapture('1.mp4')

# set resolusi video
cap.set(cv2.CAP_PROP_FRAME_WIDTH, im_width)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, im_height)


while 1:
    # buka cap supaya dapat dibaca frame
    ret, frame = cap.read()
    # konversi BGR ke HSV untuk thresholding
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # batas bawah threshold
    lower_blue = (35, 30, 30)
    # batas atas threshold
    upper_blue = (60, 255, 255)
    # thresholding
    mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

    # Creating kernel untuk dilasi
    kernel = np.ones((5, 5), np.uint8)

    # erosi dan dilasi untuk mengurangi noise
    mask = cv2.erode(mask, kernel)
    mask = cv2.dilate(mask, kernel)

    # Yang harus dilakukan adalah beberapa langkah sebagai berikut:
    ### Cari contour dari mask ###
    # gunakan metode cv2.findContours()
    contours, hierarchy = cv2.findContours(mask,
                                           cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    ### Sort contour ###
    # gunakan metode cv2.sorted()
    # cv2.sorted()

    # menggambar tiap kontur yang ditemukan
    for i in range(len(contours)):
        ### Cari 4 titik yang akan dihubungkan menjadi sebuah kotak ###
        # gunakan metode cv2.boundingRect()
        x, y, w, h = cv2.boundingRect(contours[i])

        ### Gambarlah kotak berdasarkan 4 titik tsb pada img_new ###
        # gunakan metode cv2.rectangle()
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

        ### Tampilkan hasil ###
        # video frame
        cv2.imshow("Video", frame)
        # video masking
        cv2.imshow("Video mask", mask)

    # key untuk keluar dari stream
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        cv2.DestroyWindow("video")
        break

# melepaskan cap dan menutup semua window
cap.release()
cv2.destroyAllWindows()
