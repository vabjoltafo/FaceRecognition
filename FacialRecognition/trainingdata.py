import os
import pickle
import threading
from tkinter import messagebox, HORIZONTAL, Toplevel, Label
from tkinter.ttk import Progressbar

import cv2
import face_recognition
import imutils.paths as paths


class TrainForm:

    def __init__(self, root):
        self.dataset = ".//Image_DataSet//"
        self.module = ".//FacialRecognition//pickles//encoding1.pickle"
        self.imagepaths = list(paths.list_images(self.dataset))
        self.knownEncodings = []
        self.knownNames = []
        self.value = 0
        self.root = root

        messagebox.showinfo('Info', 'Janë gjithsej ' + str(len(self.imagepaths)) + ' të dhëna per tu trajnuar!')
        MsgBox = messagebox.askquestion('Info', 'Dëshironi të vazhdoni me trajnimin e të dhenave?', icon='warning')

        if MsgBox == 'yes':
            self.runTrainForm()
            self.threadUpdate = threading.Thread(target=self.updatePickle, args=())
            self.threadUpdate.start()

    def runTrainForm(self):
        self.width = 200
        self.height = 100
        self.toplevel_dialog = Toplevel(self.root)
        self.toplevel_dialog.minsize(self.width, self.height)
        screen_width = self.toplevel_dialog.winfo_screenwidth()
        screen_height = self.toplevel_dialog.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (screen_height / 2) - (self.height / 2)
        self.toplevel_dialog.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        self.toplevel_dialog.transient(self.root)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)

        self.label = Label(self.toplevel_dialog,text='Trajnimi i të dhënave').pack()
        self.progresBar = Progressbar(self.toplevel_dialog, orient=HORIZONTAL, variable=self.value,
                                          length=100)

        self.progresBar.place(x=52, y=40)
        self.labelValue = Label(self.toplevel_dialog)
        self.labelValue.place(x=40, y=80)

    def updatePickle(self):
        for (i, imagePath) in enumerate(self.imagepaths):
            self.labelValue['text'] = "Procesimi i  imazhit {}/{}".format(i + 1, len(self.imagepaths))
            # print("processing image {}/{}".format(i + 1, len(self.imagepaths)))
            self.progresBar['value'] = int((i/len(self.imagepaths))*100)
            name = imagePath.split(os.path.sep)[-2]
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb, model="hog")
            encodings = face_recognition.face_encodings(rgb, boxes)
            for encoding in encodings:
                self.knownEncodings.append(encoding)
                self.knownNames.append(name)
                # print("[INFO] serializing encodings...")
                data = {"encodings": self.knownEncodings, "names": self.knownNames}
                output = open(self.module, "wb")
                pickle.dump(data, output)
                output.close()
        self.progresBar.stop()
        messagebox.showinfo('Mesazh!', 'Trajnimi i të dhënave përfundoi!')
        self.Close_Toplevel()

    def Close_Toplevel(self):
        self.toplevel_dialog.destroy()


# def train(root):
#     dataset = ".//Image_DataSet//"
#     module = ".//FacialRecognition//pickles//encoding1.pickle"
#     imagepaths = list(paths.list_images(dataset))
#     knownEncodings = []
#     knownNames = []
#     messagebox.showinfo('Info','Janë gjithsej '+ str(len(imagepaths)) + ' të dhëna për tu trajnuar!')
#     MsgBox = messagebox.askquestion('Info', 'Dëshironi të vazhdoni me trajnimin e të dhënave?', icon='warning')
#
#     if MsgBox == 'yes':
#         # tk = Tk()
#
#         for (i, imagePath) in enumerate(imagepaths):
#             print("processing image {}/{}".format(i + 1,len(imagepaths)))
#             # progresBar['value'] = i+1
#             name = imagePath.split(os.path.sep)[-2]
#             image = cv2.imread(imagePath)
#             rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             boxes = face_recognition.face_locations(rgb, model= "hog")
#             encodings = face_recognition.face_encodings(rgb, boxes)
#             for encoding in encodings:
#                knownEncodings.append(encoding)
#                knownNames.append(name)
#                print("[INFO] serializing encodings...")
#                data = {"encodings": knownEncodings, "names": knownNames}
#                output = open(module, "wb")
#                pickle.dump(data, output)
#                output.close()
#
#         # mainloop()
#         messagebox.showinfo('Mesazh!','Trajnimi i të dhënave perfundoi!')

