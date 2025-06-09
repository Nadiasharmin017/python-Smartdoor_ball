import cv2
import face_recognition
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    faces = face_recognition.face_locations(frame)
    print(faces)
    cv2.imshow("Smart Doorball",frame)
    # pressing the q key will close the window other wise it will be running infinite loop
    if cv2.waitKey(10) == ord("q"):
        break
    # face recognition and face detection fornt on the cemera