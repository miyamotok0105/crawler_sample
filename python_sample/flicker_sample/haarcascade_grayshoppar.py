#python2
#python haarcascade_any.py haarcascade_eye.xml
import cv2
import sys

img = cv2.imread('Grace_Hopper.jpg', cv2.IMREAD_COLOR)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
cv2.imwrite('Grace_Hopper_.jpg', img)


# When everything is done, release the capture
# video_capture.release()
cv2.destroyAllWindows()