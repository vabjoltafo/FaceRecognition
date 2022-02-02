from tkinter import messagebox as tkMessageBox, Tk, StringVar, Label, Entry, Button
import PIL.Image
import PIL.ImageTk
from Layout import MainGui, MainForActivity
from Repositories.UserRepository import findTheUser


class LoginForm:

    def __init__(self):
        self.root = Tk()
        self.root.iconbitmap(default='Layout\\images\\Icon.ico')
        self.width = 400
        self.height = 480
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x = (self.screen_width/2) - (self.width/2)
        self.y = (self.screen_height/2) - (self.height /2)


        self.root.geometry('%dx%d+%d+%d' % (self.width,self.height ,self.x,self.y))
        self.root.title("Face Recognition")
        self.root.resizable(0, 0)
        self.root.configure(background='#ecf0f1')
         
        #variablat
        self.USERNAME = StringVar()
        self.PASSWORD = StringVar()

        #komponentet

        faceImage = PIL.Image.open("Layout\\images\\Icon.png")
        faceImage = faceImage.resize((300, 300), PIL.Image.ANTIALIAS)
        self.faceImage = PIL.ImageTk.PhotoImage(faceImage)

        self.ShowfaceImage = Label(width=200, height=80, border='0', bg='#ecf0f1',
                                image=self.faceImage).place(x=100, y=10)


        self.usernameLabel = Label(self.root, text = "Përdoruesi",font = ("Sans-Serif", 16),
                                   fg ='black', bg='#ecf0f1').place(x=15,y=105)


        self.usernameField = Entry(self.root, bg='#d8d8fe',textvariable=self.USERNAME,
                                   fg='black',font=("Sans-Serif", 13), justify='center').place(x=15,y=140,width=360,height=40)


        self.passwordLabel = Label(self.root,text = "Fjalëkalimi",font = ("Sans-Serif", 16),
                                   fg ='black', bg='#ecf0f1').place(x=15,y=225)


        self.passwordField = Entry(self.root,width = 40, bg ='#d8d8fe', textvariable = self.PASSWORD,
                                   fg='black',show="*",font=("Sans-Serif", 13), justify='center').place(x=15,y=260,width=360,height=40)



        hyrImage = PIL.Image.open("Layout\\images\\Hyr.png")
        hyrImage = hyrImage.resize((600, 455), PIL.Image.ANTIALIAS)
        self.hyrImage = PIL.ImageTk.PhotoImage(hyrImage)

        self.loginButton = Button(width=80, height=35,border='0', bg = '#ecf0f1',
                                 command = self.login, image = self.hyrImage).place(x=150, y=330)

        filloImage = PIL.Image.open("Layout\\images\\FilloButton.png")
        filloImage = filloImage.resize((600, 455), PIL.Image.ANTIALIAS)
        self.filloImage = PIL.ImageTk.PhotoImage(filloImage)

        self.startButton = Button(width=80, height=35, border = '0', bg='#ecf0f1',
                                  command=self.start, image = self.filloImage).place(x=150, y=380)

        self.FaceRecognitionLabel = Label(self.root, text = "Face Recognition © 2020", font = ("Sans-Serif", 10), fg='black',
                                          bg='#ecf0f1').place(x=120, y=450)

    def start(self):
        self.root.destroy()
        main = MainForActivity.MainForActivity()
        main.runMainActivityLayout()

    def login(self):
        
            if self.USERNAME.get() == '' or self.PASSWORD.get() == '' :

                tkMessageBox.showerror("Gabim", "Plotësoni fushat!")
            else:
                tuple = ()
                tuple = findTheUser(self.USERNAME.get(),self.PASSWORD.get())

                if tuple is not None :
                    self.root.destroy()
                    main = MainGui.MainGui(str(tuple[1]))
                    main.runMainLayout()
                else:
                    tkMessageBox.showerror("Gabim", "Të dhënat e vendosuara janë gabim!")

    def runLoginForm(self):
        self.root.mainloop()
          

