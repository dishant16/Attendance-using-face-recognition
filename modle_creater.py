import os
import cv2
import numpy as np
from PIL import Image

import pickle
face1 = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# below function work same as os.getcwd()
base_dir = os.path.dirname(os.path.abspath(__file__))
# to use join two or more path
label_ = {}
count = 0
y_labels = []
x_train = []
final_path = os.path.join(base_dir, "faces")  # to join two or more paths
rec = cv2.face.LBPHFaceRecognizer_create()

for (a, b, c) in os.walk(final_path):        # here a is path ,b is dir name ,c is file name
    for file in c:
        if file.endswith("jpg"):
            path = os.path.join(a, file)
            # here os.path.basename() will give us base directory assume that our path is
            # 'D:\\programmes\\opencv2' it will return only opencv2
            # os.path.dirname() return dir name according to our path it wil return
            # 'D:\\programmes'
            # in this script our path is D:\programmes\opencv2\faces\BHADRESH\38.jpg
            # here os.path.dirname(path) gives D:\programmes\opencv2\faces\BHADRESH
            # os.path.basename("D:\programmes\opencv2\faces\BHADRESH") gives BHADRESH
            # insted of using path we can use a
            label = os.path.basename(os.path.dirname(path))
            print(label, path)
            if label not in label_:
                label_[label] = count
                count += 1
            id_ = label_[label]
            print(label_)
            pil_Image = Image.open(path).convert("L")
            size = (550, 550)
            final_image = pil_Image.resize(size)
            image_array = np.array(final_image, "uint8")
            face_detector = face1.detectMultiScale(image_array, 1.32, 5)

            for (x, y, w, h) in face_detector:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
with open("labels.pickle", "wb") as f:
    pickle.dump(label_, f)
rec.train(x_train, np.array(y_labels))
rec.save("train.yml")
