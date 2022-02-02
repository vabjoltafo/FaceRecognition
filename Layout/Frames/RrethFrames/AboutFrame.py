import webbrowser
from tkinter import Frame, Label

import PIL.Image
import PIL.ImageTk


class AboutFrame(Frame):

    def __init__(self,root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600

        #thirrja e  metodave
        self.initCredits()
        self.initReferences()

    def initCredits(self):

        IconImage = PIL.Image.open("Layout\\images\\Icon.png")
        IconImage = IconImage.resize((250, 250), PIL.Image.ANTIALIAS)
        self.IconImage = PIL.ImageTk.PhotoImage(IconImage)

        self.ShowIconImage = Label(width=200, height=80, border='0', bg='#ecf0f1',
                                   image=self.IconImage).place(x=260, y=40)

        self.nameLabel = Label(text="Face Recognition © 2020", font=("Sans-Serif", 25,'bold')).place(x=400, y=60)
        self.versionLabel = Label(text="Version 1.0", font=("Sans-Serif", 13,'bold')).place(x=540, y=110)
        self.frame = Frame(width=700, height=2,highlightbackground="black",highlightthickness = 1, bd=1).place(x=220, y=210)
        self.ncopyLabel = Label(text="All Rights Reserved to Ismail Dama and Vabjol Tafo",
                                font=("Sans-Serif", 13, 'bold')).place(x=365, y=550)

    def callback(self, event):
        self.url = event.widget.cget("text")
        webbrowser.open_new(self.url)


    def initReferences(self):
        self.refs = Label(text="Referencat:", font=("Sans-Serif", 15,'bold')).place(x=220, y=220)

        self.ref1 = Label(text="OpenCv:", font=("Sans-Serif", 10,'bold')).place(x=220, y=250)
        self.link1 = Label(text=r"https://docs.opencv.org/master/d6/d00/tutorial_py_root.html", fg="blue",cursor="hand2")
        self.link1.place(x=280, y=250)

        self.ref2 = Label(text="Tkinter:", font=("Sans-Serif", 10, 'bold')).place(x=220, y=270)
        self.link2 = Label(text=r"https://docs.python.org/3.7/library/tkinter.html", fg="blue",cursor="hand2")
        self.link2.place(x=280, y=270)

        self.ref3 = Label(text="Tksheet:", font=("Sans-Serif", 10, 'bold')).place(x=220, y=290)
        self.link3 = Label(text=r"https://github.com/ragardner/tksheet", fg="blue",cursor="hand2")
        self.link3.place(x=280, y=290)

        self.ref4 = Label(text="TkCalendar:", font=("Sans-Serif", 10, 'bold')).place(x=220, y=310)
        self.link4 = Label(text=r"https://pypi.org/project/tkcalendar", fg="blue", cursor="hand2")
        self.link4.place(x=300, y=310)

        self.ref5 = Label(text="FaceRecognition:", font=("Sans-Serif", 10, 'bold')).place(x=220, y=330)
        self.link5 = Label(text=r"https://github.com/ageitgey/face_recognition", fg="blue", cursor="hand2")
        self.link5.place(x=335, y=330)

        self.link1.bind("<Button-1>", self.callback)
        self.link2.bind("<Button-1>", self.callback)
        self.link3.bind("<Button-1>", self.callback)
        self.link4.bind("<Button-1>", self.callback)
        self.link5.bind("<Button-1>", self.callback)



