from tkinter import Frame, Label, Button, Toplevel, StringVar, Entry, ttk, messagebox
import PIL
from Enums import UserType
from Layout.Frames.PerdoruesFrames.UserTable import UserTable
from Repositories.UserRepository import findTheUser, insertUser, updateUser, getAllUsers, deleteUser


class UserFrame(Frame):

    def __init__(self,root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600

        self.nameLabel = Label(text="Përdoruesit ", font=("Sans-Serif", 25, 'bold'))
        self.nameLabel.place(x=208, y=30)

        ShtoImage = PIL.Image.open("Layout\\images\\ShtoButton.png")
        ShtoImage = ShtoImage.resize((400, 350), PIL.Image.ANTIALIAS)
        self.ShtoImage = PIL.ImageTk.PhotoImage(ShtoImage)

        self.insertButton = Button(width=70, bd=0, height=40, image=self.ShtoImage,
                                  command=self.addUser).place(x=200, y=117)



        EleminoImage = PIL.Image.open("Layout\\images\\EleminoButton.png")
        EleminoImage = EleminoImage.resize((400, 320), PIL.Image.ANTIALIAS)
        self.EleminoImage = PIL.ImageTk.PhotoImage(EleminoImage)

        self.deleteButton = Button(width=70, height=40, bd=0, image=self.EleminoImage,
                                   command=self.deleteUser).place(x=270, y=120)


        NdryshoImage = PIL.Image.open("Layout\\images\\NdryshoButton.png")
        NdryshoImage = NdryshoImage.resize((400, 320), PIL.Image.ANTIALIAS)
        self.NdryshoImage = PIL.ImageTk.PhotoImage(NdryshoImage)

        self.editButton = Button( width=80, height=40, bd=0, image=self.NdryshoImage,
                                  command=self.editUser).place(x=348, y=120)


        self.table = UserTable()
        self.table.place(x=200, y=170)


    def addUser(self):

        self.width = 500
        self.height = 400
        self.toplevel_dialog = Toplevel(self)
        self.toplevel_dialog.minsize(self.width, self.height)
        self.screen_width = self.toplevel_dialog.winfo_screenwidth()
        self.screen_height = self.toplevel_dialog.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.toplevel_dialog.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.toplevel_dialog.transient(self)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)

        self.toplevel_dialog_label = Label(self.toplevel_dialog, text='Shto përdorues',
                                               font=("Sans-Serif", 15, 'bold'))
        self.toplevel_dialog_label.place(x=100, y=5)

        NAME = StringVar()
        SURNAME = StringVar()
        USERNAME = StringVar()
        PASSWORD = StringVar()
        USER_TYPE = StringVar()

        self.nameLabel = Label(self.toplevel_dialog, text='Emri', font=('Sans-Serif', 15, 'bold')).place(x=40, y=70)
        self.nameField = Entry(self.toplevel_dialog, width=45, textvariable=NAME)
        self.nameField.place(x=165, y=70, height=25)

        self.surnameLabel = Label(self.toplevel_dialog, text='Mbiemri', font=('Sans-Serif', 15, 'bold')).place(x=40,
                                                                                                                   y=120)
        self.surnameField = Entry(self.toplevel_dialog, width=45, textvariable=SURNAME)
        self.surnameField.place(x=165, y=120, height=25)

        self.userNameLabel = Label(self.toplevel_dialog, text='Përdoruesi', font=('Sans-Serif', 15, 'bold')).place(x=40,y=170)

        self.userNameField = Entry(self.toplevel_dialog, width=45, textvariable=USERNAME)
        self.userNameField.place(x=165, y=170, height=25)

        self.passwordLabel = Label(self.toplevel_dialog, text='Fjalëkalimi', font=('Sans-Serif', 15, 'bold')).place(x=40,
                                                                                                                y=220)
        self.paswordField = Entry(self.toplevel_dialog, width=45, textvariable=PASSWORD)
        self.paswordField.place(x=165, y=220, height=25)

        self.userTypeLabel = Label(self.toplevel_dialog, text='Tipi', font=('Sans-Serif', 15, 'bold')).place(x=40,
                                                                                                                 y=270)
        self.userTypeCombo = ttk.Combobox(self.toplevel_dialog, width=42, values=UserType.userTypeList,
                                          textvariable=USER_TYPE)
        self.userTypeCombo.place(x=165, y=270, height=25)


        RuajImage = PIL.Image.open("Layout\\images\\RuajButton.png")
        RuajImage = RuajImage.resize((450, 300), PIL.Image.ANTIALIAS)
        self.RuajImage = PIL.ImageTk.PhotoImage(RuajImage)
        self.toplevel_dialog_yes_button = Button(self.toplevel_dialog, image=self.RuajImage, bd=0, width=55,
                                                 height=45, command=lambda:self.insertUserToDb(NAME, SURNAME, USERNAME, PASSWORD, USER_TYPE))

        self.toplevel_dialog_yes_button.place(x=190, y=350)

        AnuloImage = PIL.Image.open("Layout\\images\\AnuloButton.png")
        AnuloImage = AnuloImage.resize((400, 300), PIL.Image.ANTIALIAS)
        self.AnuloImage = PIL.ImageTk.PhotoImage(AnuloImage)

        self.toplevel_dialog_no_button = Button(self.toplevel_dialog, bd=0, height=45, width=55,
                                                    image=self.AnuloImage, command=self.Close_Toplevel)

        self.toplevel_dialog_no_button.place(x=260, y=350)


    def Close_Toplevel(self):
        self.toplevel_dialog.destroy()


    def insertUserToDb(self, name, surname, username, password, userType):
        if name.get() == '' or surname.get() == '' or username.get == '' or password.get() == '' or userType.get() == '':
            messagebox.showerror("Gabim", "Plotësoni të gjitha fushat!")
        else:
            if findTheUser(username.get(), password.get()):
                messagebox.showerror("Gabim", "Perdoruesi i plotësuar ekziston!")
            else:
                insertUser(name.get(), surname.get(), username.get(), password.get(), userType.get())
                # messagebox.showinfo("Info", "Përdoruesi u shtua me sukses!")
                self.table = UserTable()
                self.table.place(x=200, y=165)
                self.Close_Toplevel()


    def updateUser(self, name, surname, username, password, userType):
        if findTheUser(username.get(), password.get()) is None:
            updateUser(self.userID , name.get(), surname.get(), username.get(), password.get(), userType.get())
            data = getAllUsers()
            self.table = UserTable()
            self.table.place(x=200, y=170)
            self.table.updateTable(data)
            self.Close_Toplevel()
        else:
            if findTheUser(username.get(), password.get())[0] == self.userID:
                updateUser(self.userID, name.get(), surname.get(), username.get(), password.get(), userType.get())
                data = getAllUsers()
                # self.table = UserTable()
                # self.table.place(x=200, y=170)
                self.table.updateTable(data)
                self.Close_Toplevel()
            else:
                messagebox.showerror("Gabim", "Perdoruesi i plotësuar ekziston!")


    def deleteUser(self):
        if self.table.getResponse() is ():
            messagebox.showerror('Kujdes!', 'Zgjidhni një përdorues në tabelë!')
        else:
            index = int(self.table.getResponse()[1])
            data = self.table.getData()
            username = data[index][2]
            password = data[index][3]
            userId = findTheUser(username, password)[0]

            MsgBox = messagebox.askquestion('Fshirje', 'Jeni i sigurt që doni të fshini përdoruesin '
                                            + data[index][2] + ' ' + data[index][3] + '?',
                                            icon='warning')
            if MsgBox == 'yes':
                deleteUser(userId)
                # messagebox.showinfo('Info', 'Përdoruesi u fshi me sukses!')
                data = getAllUsers()
                # self.table = UserTable()
                # self.table.place(x=200, y=170)
                self.table.updateTable(data)



    def editUser(self):
        if self.table.getResponse() is ():

            messagebox.showerror('Kujdes!', 'Zgjidhni një përdorues në tabelë!')

        else:
            index = int(self.table.getResponse()[1])
            data = self.table.getData()
            username = data[index][2]
            password = data[index][3]
            user = findTheUser(username, password)
            self.userID = user[0]
            self.width = 500
            self.height = 400
            self.toplevel_dialog = Toplevel(self)
            self.toplevel_dialog.minsize(self.width, self.height)
            self.screen_width = self.toplevel_dialog.winfo_screenwidth()
            self.screen_height = self.toplevel_dialog.winfo_screenheight()
            self.x = (self.screen_width / 2) - (self.width / 2)
            self.y = (self.screen_height / 2) - (self.height / 2)
            self.toplevel_dialog.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
            self.toplevel_dialog.transient(self)
            self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)

            self.toplevel_dialog_label = Label(self.toplevel_dialog, text='Ndrysho të dhënat e përdoruesit', font=("Sans-Serif", 15,'bold'))
            self.toplevel_dialog_label.place(x=100, y=5)

            NAME = StringVar()
            SURNAME = StringVar()
            USERNAME = StringVar()
            PASSWORD = StringVar()
            USER_TYPE = StringVar()

            NAME.set(user[4])
            SURNAME.set(user[5])
            USERNAME.set(user[1])
            PASSWORD.set(user[2])
            USER_TYPE.set(user[3])

            self.nameLabel = Label(self.toplevel_dialog, text='Emri', font=('Sans-Serif', 15, 'bold')).place(x=40, y=70)
            self.nameField = Entry(self.toplevel_dialog, width=45, textvariable=NAME)
            self.nameField.place(x=165, y=70, height=25)

            self.surnameLabel = Label(self.toplevel_dialog, text='Mbiemri', font=('Sans-Serif', 15, 'bold')).place(x=40,
                                                                                                                   y=120)
            self.surnameField = Entry(self.toplevel_dialog, width=45, textvariable=SURNAME)
            self.surnameField.place(x=165, y=120, height=25)

            self.userNameLabel = Label(self.toplevel_dialog, text='Përdoruesi', font=('Sans-Serif', 15, 'bold')).place(
                x=40, y=170)

            self.userNameField = Entry(self.toplevel_dialog, width=45, textvariable=USERNAME)
            self.userNameField.place(x=165, y=170, height=25)

            self.passwordLabel = Label(self.toplevel_dialog, text='Fjalëkalimi', font=('Sans-Serif', 15, 'bold')).place(
                x=40,
                y=220)
            self.paswordField = Entry(self.toplevel_dialog, width=45, textvariable=PASSWORD)
            self.paswordField.place(x=165, y=220, height=25)

            self.userTypeLabel = Label(self.toplevel_dialog, text='Tipi', font=('Sans-Serif', 15, 'bold')).place(x=40,
                                                                                                                 y=270)
            self.userTypeCombo = ttk.Combobox(self.toplevel_dialog, width=42, values=UserType.userTypeList,
                                              textvariable=USER_TYPE)
            self.userTypeCombo.place(x=165, y=270, height=25)

            RuajImage = PIL.Image.open("Layout\\images\\RuajButton.png")
            RuajImage = RuajImage.resize((450, 300), PIL.Image.ANTIALIAS)
            self.RuajImage = PIL.ImageTk.PhotoImage(RuajImage)
            self.toplevel_dialog_yes_button = Button(self.toplevel_dialog, image=self.RuajImage, bd=0, width=55,
                                                     height=45,
                                                     command=lambda: self.updateUser(NAME, SURNAME, USERNAME,
                                                                                         PASSWORD, USER_TYPE))

            self.toplevel_dialog_yes_button.place(x=190, y=350)

            AnuloImage = PIL.Image.open("Layout\\images\\AnuloButton.png")
            AnuloImage = AnuloImage.resize((400, 300), PIL.Image.ANTIALIAS)
            self.AnuloImage = PIL.ImageTk.PhotoImage(AnuloImage)

            self.toplevel_dialog_no_button = Button(self.toplevel_dialog, bd=0, height=45, width=55,
                                                    image=self.AnuloImage, command=self.Close_Toplevel)

            self.toplevel_dialog_no_button.place(x=260, y=350)
