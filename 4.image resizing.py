import cv2
img=cv2.imread("photo.jpeg")
resize=cv2.resize(img,(400,400))
cv2.imshow("Resize Image",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()