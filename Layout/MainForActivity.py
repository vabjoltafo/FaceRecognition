import argparse
from tkinter import Tk, Button, Frame

import PIL.Image
import PIL.ImageTk
from imutils.video import VideoStream

from Layout import LoginForm
from Layout.Frames.DaljaFrames.ExitFaceFrame import ExitFaceFrame
from Layout.Frames.HyrjaFrames.FaceFrame import FaceFrame


class MainForActivity:

    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap(default='Layout\\images\\Icon.ico')
        self.width = 950
        self.height = 600
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.root.title("Face Recognition")
        self.root.resizable(0, 0)
        self.buildMainNavBar()

    def buildMainNavBar(self):
        self.frame = Frame(self.root, width=220, height=600)
        self.frame.place(x=0, y=0)
        hyrimg = PIL.Image.open("Layout\\images\\RegjHyrjeButton.png")
        hyrimg = hyrimg.resize((600, 455), PIL.Image.ANTIALIAS)
        self.hyrimg = PIL.ImageTk.PhotoImage(hyrimg)

        self.hyrButton = Button(self.frame, width=180,height=35, bg='#ecf0f1',border = '0',
                                  image = self.hyrimg, command=self.runFaceRecognitionEntrance).place(x=40, y=40)

        dilimg = PIL.Image.open("Layout\\images\\RegjDaljeButton.png")
        dilimg = dilimg.resize((600, 455), PIL.Image.ANTIALIAS)
        self.dilimg = PIL.ImageTk.PhotoImage(dilimg)

        self.dilButton = Button(self.frame, width=180,height=35, bg='#ecf0f1', border = '0',
                                  image = self.dilimg, command=self.runFaceRecognitionExit).place(x=40, y=100)

        kthehuimg = PIL.Image.open("Layout\\images\\KthehuButton.png")
        kthehuimg = kthehuimg.resize((600, 455), PIL.Image.ANTIALIAS)
        self.kthehuimg = PIL.ImageTk.PhotoImage(kthehuimg)

        self.kthehuButton = Button(self.frame, width=110,height=35, bg='#ecf0f1', border = '0',
                                  image =self.kthehuimg,command=self.exitActivity).place(x=40, y=160)


    def runMainActivityLayout(self):
        self.root.mainloop()


    def removeAllFrames(self):
        for widget in self.root.winfo_children():
            if widget is not self.frame:
                widget.destroy()


    def exitActivity(self):
        self.root.destroy()
        log = LoginForm.LoginForm()
        log.runLoginForm()


    def runFaceRecognitionEntrance(self):
        self.removeAllFrames()
        ap = argparse.ArgumentParser()
        ap.add_argument("-p", "--picamera", type=int, default=-1,
                        help="whether or not the Raspberry Pi camera should be used")
        args = vars(ap.parse_args())
        print("[INFO] warming up camera...")
        vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
        self.faceFrame = FaceFrame(vs, self.root, 728, 650, 220)


    def runFaceRecognitionExit(self):
        self.removeAllFrames()
        ap = argparse.ArgumentParser()
        ap.add_argument("-p", "--picamera", type=int, default=-1,
                        help="whether or not the Raspberry Pi camera should be used")
        args = vars(ap.parse_args())
        print("[INFO] warming up camera...")
        vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
        self.exitFaceFrame = ExitFaceFrame(vs, self.root, 728, 650, 220)