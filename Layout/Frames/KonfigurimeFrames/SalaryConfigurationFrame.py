from tkinter import Frame, Label, Entry, Button, Toplevel, StringVar, messagebox
import PIL
from Repositories.KontributeRepository import getAllKontribute, updateKontribute, insertFirstKontribut
from Utilities.DbUtility import isNumber


class SalaryConfigurationFrame(Frame):

    def __init__(self,root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.PagaLabel = Label(self, text = "Kontributet dhe Tatimi", font=("Sans-Serif", 25,'bold')).place(x=5, y=20)
        configbutton = PIL.Image.open("Layout\\images\\KonfiguroButton.png")
        configbutton = configbutton.resize((600, 450), PIL.Image.ANTIALIAS)
        self.configbutton = PIL.ImageTk.PhotoImage(configbutton)
        self.configureButton = Button(self, width=105, height=38, bd=0,
                                      command=self.openForm, image = self.configbutton).place(x=320, y=450)
        self.buildContent()

    def buildContent(self):

        self.data = getAllKontribute()

        self.kShendetsore = StringVar()
        self.kShoqerore = StringVar()
        self.TAP1 = StringVar()
        self.TAP2 = StringVar()
        self.TAP3 = StringVar()

        if self.data:
            self.kShendetsore.set(self.data[1])
            self.kShoqerore.set(self.data[2])
            self.TAP1.set(self.data[3])
            self.TAP2.set(self.data[4])
            self.TAP3.set(self.data[5])
        else:
            self.kShendetsore.set("")
            self.kShoqerore.set("")
            self.TAP1.set("")
            self.TAP2.set("")
            self.TAP3.set("")


        self.KontribShoqLabel = Label(self, text='Kontributet shoqërore(%)', font=('Sans-Serif', 15, 'bold')).place(x=80, y=140)
        self.KontribShoqEntry = Entry(self, width=45, state='disabled', textvariable=self.kShoqerore).place(x=380, y=140, height=25)

        self.KontribShendLabel = Label(self, text='Kontributet shëndetësore(%)', font=('Sans-Serif', 15, 'bold')).place(x=80, y=190)
        self.KontribShendField = Entry(self, width=45, state='disabled', textvariable=self.kShendetsore).place(x=380, y=190, height=25)

        self.Tap0Label = Label(self, text='TAP 0 - 30000 lekë', font=('Sans-Serif', 15, 'bold')).place(x=80, y=240)
        self.Tap0Entry = Entry(self, width=45, state='disabled', textvariable=self.TAP1).place(x=380, y=240, height=25)

        self.Tap1Label = Label(self, text='TAP 30000 - 150000 lekë', font=('Sans-Serif', 15, 'bold')).place(x=80, y=290)
        self.Tap1Entry = Entry(self, width=45, state='disabled', textvariable=self.TAP2).place(x=380, y=290, height=25)

        self.Tap2Label = Label(self, text='TAP mbi 150000 lekë', font=('Sans-Serif', 15, 'bold')).place(x=80, y=340)
        self.Tap2Entry = Entry(self, width=45, state='disabled', textvariable=self.TAP3).place(x=380, y=340, height=25)

    def openForm(self):
        self.width = 670
        self.height = 430
        self.toplevel_dialog = Toplevel(self)
        self.toplevel_dialog.minsize(self.width, self.height)
        self.screen_width = self.toplevel_dialog.winfo_screenwidth()
        self.screen_height = self.toplevel_dialog.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.toplevel_dialog.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.toplevel_dialog.transient(self)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)

        self.toplevel_dialog_label = Label(self.toplevel_dialog, text='Ndrysho',
                                           font=("Sans-Serif", 15, 'bold')).pack()

        self.KontribShoqLabel = Label(self.toplevel_dialog, text='Kontributet shoqërore(%)', font=('Sans-Serif', 15, 'bold')).place(
            x=20, y=50)
        self.KontribShoqEntry1 = Entry(self.toplevel_dialog, width=45, textvariable=self.kShoqerore).place(x=340, y=50, height=25)

        self.KontribShendLabel = Label(self.toplevel_dialog, text='Kontributet shëndetësore(%)', font=('Sans-Serif', 15, 'bold')).place(
            x=20, y=100)
        self.KontribShendField1 = Entry(self.toplevel_dialog, width=45,textvariable=self.kShendetsore).place(x=340, y=100, height=25)

        self.Tap0Label = Label(self.toplevel_dialog, text='TAP 0 - 30000 lekë', font=('Sans-Serif', 15, 'bold')).place(x=20, y=150)
        self.Tap0Entry1 = Entry(self.toplevel_dialog, width=45, textvariable=self.TAP1).place(x=340, y=150, height=25)

        self.Tap1Label = Label(self.toplevel_dialog, text='TAP 30000 - 150000 lekë', font=('Sans-Serif', 15, 'bold')).place(x=20, y=200)
        self.Tap1Entry1 = Entry(self.toplevel_dialog, width=45, textvariable=self.TAP2).place(x=340, y=200, height=25)


        self.Tap2Label = Label(self.toplevel_dialog, text='TAP mbi 150000 lekë', font=('Sans-Serif', 15, 'bold')).place(x=20, y=250)
        self.Tap2Entry1 = Entry(self.toplevel_dialog, width=45, textvariable=self.TAP3).place(x=340, y=250, height=25)

        RuajImage = PIL.Image.open("Layout\\images\\RuajButton.png")
        RuajImage = RuajImage.resize((450, 300), PIL.Image.ANTIALIAS)
        self.RuajImage = PIL.ImageTk.PhotoImage(RuajImage)
        self.toplevel_dialog_yes_button = Button(self.toplevel_dialog, image=self.RuajImage, bd=0, width=55,
                                                 height=45, command=self.onSave)

        self.toplevel_dialog_yes_button.place(x=270, y=350)

        AnuloImage = PIL.Image.open("Layout\\images\\AnuloButton.png")
        AnuloImage = AnuloImage.resize((400, 300), PIL.Image.ANTIALIAS)
        self.AnuloImage = PIL.ImageTk.PhotoImage(AnuloImage)

        self.toplevel_dialog_no_button = Button(self.toplevel_dialog, bd=0, height=45, width=55,
                                                image=self.AnuloImage, command=self.Close_Toplevel)

        self.toplevel_dialog_no_button.place(x=340, y=350)


    def Close_Toplevel(self):
        self.toplevel_dialog.destroy()


    def onSave(self):
        try:
            if isNumber(float(self.kShendetsore.get())) is True and isNumber(float(self.kShoqerore.get())) is True \
                    and isNumber(float(self.TAP1.get())) is True and isNumber(float(self.TAP2.get())) is True \
                    and isNumber(float(self.TAP3.get())) is True:

                if getAllKontribute():
                    updateKontribute(self.kShendetsore.get(), self.kShoqerore.get(),
                                     self.TAP1.get(), self.TAP2.get(), self.TAP3.get())
                else:
                    insertFirstKontribut(self.kShendetsore.get(), self.kShoqerore.get(),
                                     self.TAP1.get(), self.TAP2.get(), self.TAP3.get())

                self.toplevel_dialog.destroy()

        except ValueError:
            messagebox.showwarning('Kujdes!', 'Te dhenat e vendosura nuk jane numra')
            if self.data:
                self.kShendetsore.set(self.data[1])
                self.kShoqerore.set(self.data[2])
                self.TAP1.set(self.data[3])
                self.TAP2.set(self.data[4])
                self.TAP3.set(self.data[5])
            else:
                self.kShendetsore.set("")
                self.kShoqerore.set("")
                self.TAP1.set("")
                self.TAP2.set("")
                self.TAP3.set("")



