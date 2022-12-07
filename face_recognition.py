import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_faces.xml')

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')
people = ['Ben Affleck', 'Elton John', 'Jerry Seinfeld', 'Madonna', 'Mindy Kaling']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'/Users/adityabangar/Desktop/Learning Stuff/ML_Practice/openCV_learn/Resources/Faces/val/madonna/5.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#Detect the face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {label}, with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness = 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 1)

cv.imshow('Detected Face', img)

cv.waitKey(0)