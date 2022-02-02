from tkinter import Frame, Label, Button

import PIL.Image
import PIL.ImageTk

from FacialRecognition.trainingdata import TrainForm


class TrainDataFrame(Frame):

    def __init__(self,root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.nameLabel = Label(text = "Trajno të dhënat ", font=("Sans-Serif", 25,'bold')).place(x=208, y=45)

        self.label1 = Label(text='Trajnimi i të dhënave ka të bëjë me të dhëna të '
                                 'etiketuara që përdoren për të trajnuar algoritmet e',
                            font=("Sans-Serif", 13)).place(x=210, y=90)
        self.label2 = Label(text='të mësuarit të makinerisë dhe për të rritur saktësinë. '
                                 'Trajnimi i të dhënave sugjerohet të realizohet',
                            font=("Sans-Serif", 13)).place(x=210, y=112)
        self.label3 = Label(text='pas një shtimi, eleminimi ose ndryshimi të të dhënave të një punonjësi.',
                            font=("Sans-Serif", 13)).place(x=210, y=134)

        trainImage = PIL.Image.open('Layout\\images\\traindata.png')
        trainImage = trainImage.resize((650, 600), PIL.Image.ANTIALIAS)
        self.trainImage = PIL.ImageTk.PhotoImage(trainImage)

        self.trainButton = Button(bg='#ecf0f1',
                                   width=320, height=100,border = 0, image = self.trainImage,
                                   command=lambda:self.trainDataSet(root)).place(x=400, y=400)


    def trainDataSet(self, root):
        trainForm = TrainForm(root)