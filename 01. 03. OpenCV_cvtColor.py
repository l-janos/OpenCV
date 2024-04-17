#Kép beolvasása File-ból
import cv2
imgc = cv2.imread("assets/imgs/Apple.png", cv2.IMREAD_COLOR)
cv2.imshow("Color", imgc)
#Szürkeárnyalat
imgr = cv2.cvtColor(imgc, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", imgr)
#Szürkéből "színes"
imgc2 = cv2.cvtColor(imgr, cv2.COLOR_GRAY2BGR)
cv2.imshow("Gray2BGR", imgc2)
cv2.waitKey(0)
#Áttérés lab színtérre
#L : Szürkeárnyalat
#a, b : (Kromatikusok), színinformációkat jelenti
imgLab = cv2.cvtColor(imgc, cv2.COLOR_BGR2Lab)
cv2.imshow("BGR2Lab", imgLab)
cv2.waitKey(0)
#Színcsatornákra bontás
L, a, b = cv2.split(imgLab)
cv2.imshow('L', L)
cv2.imshow('a', a)
cv2.imshow('b', b)
cv2.waitKey(0)