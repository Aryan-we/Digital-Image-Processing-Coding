import cv2
img=cv2.imread("photo.jpeg")
r,thresh=cv2.threshold(img,180,255,cv2.THRESH_BINARY)
print(img[100,150])
print(thresh[100,150])
cv2.imshow("Threshold Image",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()