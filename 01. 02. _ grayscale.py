import cv2
#Kép beolvasása File-ból szürkeárnxalatosként
img_gr = cv2.imread("assets/imgs/Apple.png", cv2.IMREAD_GRAYSCALE)
print(img_gr.shape)
#Képet jelenítsük meg az ablakban
cv2.imshow("img", img_gr)
cv2.imwrite("Apple_imreadColorGrayScale.png", img_gr)
cv2.waitKey(0)
img_c = cv2.imread("assets/imgs/Apple.png", cv2.IMREAD_COLOR)
img_gr2 = cv2.cvtColor(img_c,cv2.COLOR_BGR2GRAY)
cv2.imshow("kep", img_gr2)
flip = cv2.flip(img_gr2, 1)
cv2.imshow("kep", flip)
cv2.imwrite("Apple_bgr2gray_fliped.png", flip)
cv2.imwrite("Apple_bgr2gray.png", img_gr2)
cv2.waitKey(0)