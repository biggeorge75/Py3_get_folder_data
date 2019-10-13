import cv2

image = cv2.imread("kids.jpeg")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

faces = face_cascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 14)
eye = eye_cascade.detectMultiScale(image, scaleFactor = 1.3, minNeighbors = 11)

print("Faces Detected", len(faces))
print("Eyes Detected", len(eye))

for x,y,w,h in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 4)

for x,y,w,h in eye:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,0,255), 4)

cv2.imshow("Face Detected", image)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()