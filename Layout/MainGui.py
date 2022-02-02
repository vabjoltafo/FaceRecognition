import argparse
from _tkinter import TclError
from tkinter import Tk, LEFT

import PIL.Image
import PIL.ImageTk
from imutils.video import VideoStream

from Layout import LoginForm
from Layout.Frames.DaljaFrames.ExitFaceFrame import ExitFaceFrame
from Layout.Frames.DashboardFrames.DashBoardFrame import DashboardFrame
from Layout.Frames.EmployeeFrames.EmployeeFrame import EmployeeFrame
from Layout.Frames.EmployeeFrames.RegisterEmployeeFrame import *
from Layout.Frames.HyrjaFrames.FaceFrame import *
from Layout.Frames.KonfigurimeFrames.KonfigurimeFrame import KonfigurimeFrame
from Layout.Frames.PerdoruesFrames.UserFrame import UserFrame
from Layout.Frames.RaporteFrames.RaporteFrame import RaporteFrame
from Layout.Frames.RrethFrames.AboutFrame import *


class MainGui:

    #Konstruktori
    def __init__(self,user):

        self.root = Tk()
        self.root.iconbitmap(default='Layout\\images\\Icon.ico')
        self.width = 950
        self.height = 600
        self.buttonHeight= 2
        self.buttonWidth = 200
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height /2)
        self.root.geometry('%dx%d+%d+%d' % (self.width,self.height ,self.x, self.y))
        self.root.title("Face Recognition")
        self.root.resizable(0, 0)
        self.user = user
        self.buildMainNavBar()
        self.panelLayout = DashboardFrame(self.root)


        #Nderton NavBar me butona
    def buildMainNavBar(self):
        #Icona e userit
        self.frame = Frame(self.root, width=200, height=600, background="#00ba23")
        self.frame.place(x=0, y=0)
        self.load = PIL.Image.open("Layout\\images\\userImage.png")
        self.render = PIL.ImageTk.PhotoImage(self.load)
        self.imageUserButton = Button(self.frame, image=self.render,bg="#00ba23", bd=0, command=self.logOut)
        self.imageUserButton.image = self.render
        self.imageUserButton.place(width=200, height=80, x=0, y=2)

        #Emri i perdoruesit
        self.usernameLabel = Button(self.frame, text = self.user+' ▼', fg='#ffffff', bg = "#00ba23", highlightthickness = 0,
                                   bd=0,font=("Sans-Serif", 11,'bold'), command=self.logOut
                                    ).place(width=200,height=40,x=0, y=50)

        #Butonat qe mbajne modulet
        homeicon = PIL.Image.open("Layout\\images\\HomeIcon.png")
        homeicon = homeicon.resize((20, 20), PIL.Image.ANTIALIAS)
        self.homeicon = PIL.ImageTk.PhotoImage(homeicon)

        self.dashBoardButton = Button(self.frame, text=' Dashboard ', fg='#ffffff', bg="#00ba23",
                                  font=("Sans-Serif", 13, 'bold'),
                                  highlightthickness=0, bd=0, anchor='center', command=self.runDashboardFrame, image = self.homeicon,
                                   compound=LEFT).place(width=200, height=40, x=0, y=90)


        hyrjaicon = PIL.Image.open("Layout\\images\\hyrjaicon.png")
        hyrjaicon = hyrjaicon.resize((20, 20), PIL.Image.ANTIALIAS)
        self.hyrjaicon = PIL.ImageTk.PhotoImage(hyrjaicon)

        self.startButton = Button(self.frame,  text=' Hyrja          ', fg='#ffffff', bg = "#00ba23", font=("Sans-Serif", 13,'bold'),
                                  highlightthickness = 0, bd=0, anchor='center',command=self.runFaceRecognitionEntrance,
                                  image = self.hyrjaicon, compound = LEFT).place(width=200,height=40, x=0, y=130)

        daljaicon = PIL.Image.open("Layout\\images\\daljaicon.png")
        daljaicon = daljaicon.resize((20, 20), PIL.Image.ANTIALIAS)
        self.daljaicon = PIL.ImageTk.PhotoImage(daljaicon)

        self.exitButton = Button(self.frame,  text =" Dalja          ", fg = "#ffffff", bg = "#00ba23", font=("Sans-Serif", 13,'bold'),
                                highlightthickness=0, bd=0, anchor='center',
                                command = self.runFaceRecognitionExit, image = self.daljaicon, compound = LEFT).place(width=200,height=40,x=0, y=170)

        stafficon = PIL.Image.open("Layout\\images\\stafficon.png")
        stafficon = stafficon.resize((20, 20), PIL.Image.ANTIALIAS)
        self.stafficon = PIL.ImageTk.PhotoImage(stafficon)

        self.employeeButton = Button(self.frame, text = " Punonjësit  ", fg = "#ffffff", bg = "#00ba23", font=("Sans-Serif", 13,'bold'),
                                  highlightthickness=0, bd=0, anchor='center',
                                  command= self.runEmployeeFrame, image = self.stafficon, compound = LEFT).place(width=200,height=40,x=0, y=210)

        raporteicon = PIL.Image.open("Layout\\images\\raporteicon.png")
        raporteicon = raporteicon.resize((20, 20), PIL.Image.ANTIALIAS)
        self.raporteicon = PIL.ImageTk.PhotoImage(raporteicon)

        self.raporteButton = Button(self.frame,  text=' Raporte       ', fg='#ffffff', bg = "#00ba23",font=("Sans-Serif", 13,'bold'),
                                    highlightthickness = 0, bd=0, anchor='center',
                                    command=self.runRaporteFrame, image = self.raporteicon, compound = LEFT).place(width=200,height=40,x=0, y=250)


        configicon = PIL.Image.open("Layout\\images\\configicon.png")
        configicon = configicon.resize((20, 20), PIL.Image.ANTIALIAS)
        self.configicon = PIL.ImageTk.PhotoImage(configicon)

        self.configureButton = Button(self.frame, text=' Konfigurime', fg='#ffffff', bg="#00ba23",
                                    font=("Sans-Serif", 13, 'bold'),
                                    highlightthickness=0, bd=0, anchor='center',
                                    command = self.runKonfigurimeFrame, image = self.configicon, compound = LEFT).place(width=200, height=40, x=0, y=290)


        usersIcon = PIL.Image.open("Layout\\images\\usersicon.png")
        usersIcon = usersIcon.resize((20,20), PIL.Image.ANTIALIAS)
        self.usersIcon = PIL.ImageTk.PhotoImage(usersIcon)

        self.perdoruesButton = Button(self.frame, text=' Përdoruesit', fg='#ffffff', bg="#00ba23",
                                      font=("Sans-Serif", 13, 'bold'),
                                      highlightthickness=0, bd=0, anchor='center',
                                      command=self.runUserFrame,
                                      image=self.usersIcon, compound=LEFT).place(width=200, height=40, x=0, y=330)


        abouticon = PIL.Image.open("Layout\\images\\about.png")
        abouticon = abouticon.resize((20, 20), PIL.Image.ANTIALIAS)
        self.abouticon = PIL.ImageTk.PhotoImage(abouticon)

        self.rrethButton = Button(self.frame, text=' Rreth          ', fg='#ffffff', bg = "#00ba23",font=("Sans-Serif", 13,'bold'),
                                  highlightthickness = 0, bd=0, anchor='center',
                                  command= self.runAboutFrame, image = self.abouticon, compound = LEFT).place(width=200,height=40,x=0, y=370)

    #Ekzekuton dritaren kryesore
    def runMainLayout(self):
        self.root.mainloop()


    #eleminon te gjithe komponentet
    def removeAllFrames(self):
        for widget in self.root.winfo_children():
            if widget is not self.frame:
                    widget.destroy()

    #dalja nga programi
    def logOut(self):
        MsgBox = messagebox.askquestion('Dalje nga programi', 'Je i sigurt që do të dalësh nga programi?',icon='warning')
        if MsgBox == 'yes':
            self.root.destroy()
            log = LoginForm.LoginForm()
            log.runLoginForm()


    def runAboutFrame(self):
        try:
            self.removeAllFrames()
            self.panelLayout = AboutFrame(self.root)
            self.panelLayout.place(x=200, y=0)
        except TclError:
            pass


    def runRaporteFrame(self):
        try:
            self.removeAllFrames()
            self.panelLayout = RaporteFrame(self.root)
            self.panelLayout.place(x=200, y=0)
        except TclError:
            pass


    def runFaceRecognitionEntrance(self):
        try:
            self.removeAllFrames()
            ap = argparse.ArgumentParser()
            ap.add_argument("-p", "--picamera", type=int, default=-1,
                            help="whether or not the Raspberry Pi camera should be used")
            args = vars(ap.parse_args())
            print("[INFO] warming up camera...")
            vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
            self.faceFrame = FaceFrame(vs, self.root, 800, 650, 200)
        except TclError:
            pass


    def runFaceRecognitionExit(self):
        try:
            self.removeAllFrames()
            ap = argparse.ArgumentParser()
            ap.add_argument("-p", "--picamera", type=int, default=-1,
                                help="whether or not the Raspberry Pi camera should be used")
            args = vars(ap.parse_args())
            print("[INFO] warming up camera...")
            vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
            self.exitFaceFrame = ExitFaceFrame(vs, self.root, 800, 650, 200)
        except TclError:
            pass


    def runEmployeeFrame(self):
        try:
            self.removeAllFrames()
            self.panelLayout = EmployeeFrame(self.root)
            self.panelLayout.place(x=200, y=0)
        except TclError:
            pass


    def runKonfigurimeFrame(self):
        try:
            self.removeAllFrames()
            self.panelLayout = KonfigurimeFrame(self.root)
            self.panelLayout.place(x=200, y=0)
        except TclError:
            pass

    def runUserFrame(self):
        try:
            self.removeAllFrames()
            self.panelLayout = UserFrame(self.root)
            self.panelLayout.place(x=200, y=0)
        except TclError:
            pass

    def runDashboardFrame(self):
        try:
            self.removeAllFrames()
            self.panelLayout = DashboardFrame(self.root)
            self.panelLayout.place(x=200, y=0)
        except TclError:
            pass