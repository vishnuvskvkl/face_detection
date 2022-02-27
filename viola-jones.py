
import cv2 
img=cv2.imread('C:/Users/vishn/OneDrive/Pictures/Saved Pictures/Screenshot 2022-01-29 120801.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier('D:/anaconda/pkgs/libopencv-4.0.1-hbb9e17c_0/Library/etc/haarcascades/haarcascade_frontalface_alt.xml') #OpenCv pre-trained classifiers for face, eyes, smile.
detected_faces=face_cascade.detectMultiScale(gray)
for(column,row,width,height) in detected_faces:
    cv2.rectangle(img,(column,row),(column+width,row+height),(0,255,0),2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
