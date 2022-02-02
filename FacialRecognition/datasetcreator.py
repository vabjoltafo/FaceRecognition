import os
from tkinter import messagebox as tkMessageBox

import cv2

from Repositories.EmployeeRepository import insertEmployee


def createEmployee(name, surname, gender, age, position, phone, email):
    face_cascade = cv2.CascadeClassifier('.//cascades//data//haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    path = ".//Image_DataSet//"  # path were u want store the data set
    id = name +' ' + surname

    try:
        # Create target Directory
        os.mkdir(path+str(id))
        print("Directory " , path+str(id),  " Created ")
    except FileExistsError:
        print("Directory " , path+str(id) ,  " already exists")
    sampleN=0;

    while 1:

        ret, img = cap.read()
        frame = img.copy()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            sampleN=sampleN+1;

            cv2.imwrite(path+str(id)+ "\\" +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])

            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img, str(sampleN), (10,20),cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
            cv2.waitKey(100)

        cv2.imshow('img',img)

        cv2.waitKey(1)

        if sampleN > 40:

            break
    insertEmployee(name, surname, gender, age, position, phone, email)
    tkMessageBox.showinfo("Info", "Punonjësi %s %s u shtua me sukses!" % (name, surname))

    cap.release()
    cv2.destroyAllWindows()
