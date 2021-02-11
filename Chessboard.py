import cv2
import numpy as np

img1 = np.zeros((500, 500, 3), np.uint8)                                 #Creating a plain black image
img1 = cv2.rectangle(img1, (0, 500), (250, 0), (255, 255, 255), -1)      #Choosing coordinates of rectangle's diagonals with White Colour using RGB channels and completely filling it
img2 = np.zeros((500, 500, 3), np.uint8)
img2 = cv2.rectangle(img2, (500, 0), (0, 250), (255, 255, 255), -1)
img3 = np.zeros((500, 500, 3), np.uint8)
img3 = cv2.rectangle(img3, (250, 0), (0, 250), (255, 255, 255), -1)
img4 = np.zeros((500, 500, 3), np.uint8)
img4 = cv2.rectangle(img4, (125, 0), (0, 125), (255, 255, 255), -1)
img5 = np.zeros((500, 500, 3), np.uint8)
img5 = cv2.rectangle(img5, (125, 250), (250, 125), (255, 255, 255), -1)
img6 = np.zeros((500, 500, 3), np.uint8)
img6 = cv2.rectangle(img6, (250, 125), (375, 250), (255, 255, 255), -1)
img7 = np.zeros((500, 500, 3), np.uint8)
img7 = cv2.rectangle(img7, (375, 0), (500, 125), (255, 255, 255), -1)
img8 = np.zeros((500, 500, 3), np.uint8)
img8 = cv2.rectangle(img8, (125, 250), (250, 375), (255, 255, 255), -1)
img9 = np.zeros((500, 500, 3), np.uint8)
img9 = cv2.rectangle(img9, (0, 375), (125, 500), (255, 255, 255), -1)
img10 = np.zeros((500, 500, 3), np.uint8)
img10 = cv2.rectangle(img10, (375, 375), (500, 500), (255, 255, 255), -1)
img11 = np.zeros((500, 500, 3), np.uint8)
img11 = cv2.rectangle(img11, (250, 250), (375, 375), (255, 255, 255), -1)

c1 = cv2.bitwise_or(img1, img2)
c2 = cv2.bitwise_xor(c1, img3)    #2 by 2 chessboard
c3 = cv2.bitwise_xor(c2, img4)
c4 = cv2.bitwise_xor(c3, img5)
c5 = cv2.bitwise_xor(c4, img6)
c6 = cv2.bitwise_xor(c5, img7)
c7 = cv2.bitwise_xor(c6, img8)
c8 = cv2.bitwise_xor(c7, img9)
c9 = cv2.bitwise_xor(c8, img10)
chessboard = cv2.bitwise_xor(c9, img11)

cv2.imshow('c10', chessboard)


cv2.waitKey(0)
cv2.destroyAllWindows()