import glob
import os
import threading
from tkinter import Frame, Label, Button, Image, Toplevel
from tkinter.ttk import Combobox

from PIL import Image, ImageTk

from Repositories.EmployeeRepository import getAllEmployeeNameAndSurname
from Utilities.Convertors import getEmployeeFullNameList


class DatasetViewerFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.nameLabel = Label(self, text="Dataseti i punonjesve", font=("Sans-Serif", 25, 'bold'))
        self.nameLabel.place(x=5, y=20)

        self.comboLabel = Label(self, text='Punonjësit', font=("Sans-Serif", 12, 'bold'))
        self.comboLabel.place(x=5, y=98)
        listOfEmployees = getEmployeeFullNameList(getAllEmployeeNameAndSurname())
        self.entry = Combobox(self, width=16, value=listOfEmployees, font="Sans-Serif 10")
        self.entry.place(x=5, y=123)

        KerkoImage = Image.open("Layout\\images\\KerkoButton.png")
        KerkoImage = KerkoImage.resize((450, 320), Image.ANTIALIAS)
        self.KerkoPic = ImageTk.PhotoImage(KerkoImage)

        self.searchButton = Button(self, width=50, height=30, bd=0,
                                   image=self.KerkoPic, command=self.search).place(x=160, y=117)


    def search(self):
        self.threadUpdate = threading.Thread(target=self.addImages, args=())
        self.threadUpdate.start()


    def addImages(self):
        path = r'Image_DataSet/'+self.entry.get()
        self.imageFrame = Frame(self, width=750, height=410)
        COLUMNS = 9
        image_count = 0
        for infile in glob.glob(os.path.join(path, '*.jpg')):
            image_count += 1
            r, c = divmod(image_count - 1, COLUMNS)
            im = Image.open(infile)
            resized = im.resize((79, 79), Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized)
            myvar = Label(self.imageFrame, image=tkimage)
            myvar.image = tkimage
            myvar.grid(row=r, column=c)
        self.imageFrame.place(x=0, y=160)
