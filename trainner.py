import cv2

case = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def face_recognizer(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = case.detectMultiScale(gray, 1.32, 5)
    if faces is():
        return None
    for (x, y, w, h) in faces:
        croaped_faces = img[y:y+h, x:x+w]

    return croaped_faces


cap = cv2.VideoCapture(0)
count = 1
while True:

    ret, frame = cap.read()
    if face_recognizer(frame) is not None:
        count += 1
        face = cv2.resize(face_recognizer(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        File_path = "E:/project/faces/bhadresh/" + str(count) + ".jpg"
        cv2.imwrite(File_path, face)
        cv2.putText(frame, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("face", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        if count == 720:
            break
    else:
        print("face not found")
        pass
cv2.destroyAllWindows()
cap.release()









