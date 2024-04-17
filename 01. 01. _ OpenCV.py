import cv2
#OpenCV verzióra kíváncsi vagyok.
print(cv2.__version__)
#Kép beolvasása File-ból
img = cv2.imread("assets/imgs/cica.jpg")
#Kép mérete
print(img.shape)
#kép megjelenítése
'''cv2.imshow("Cica.jpg", img)
cv2.waitKey(0)'''
#Tükrözés függőleges középtengelyen
flipped = cv2.flip(img, 1)
cv2.imshow("Kep", flipped)
cv2.imwrite("assets/imgs/cica.jpg", flipped)
cv2.waitKey(0)
#Tükrözés mind a két tengelyre
flipped2 = cv2.flip(img, -1)
cv2.imshow("assets/imgs/cica.jpg", flipped2)
cv2.waitKey(0)
#Összes ablak bezárása
cv2.destroyAllWindows()