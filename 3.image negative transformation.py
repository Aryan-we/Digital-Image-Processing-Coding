import cv2
img=cv2.imread("photo.jpeg")
negative=255-img
cv2.imshow("Negative Transform Image",negative)
cv2.waitKey(0)
cv2.destroyAllWindows()