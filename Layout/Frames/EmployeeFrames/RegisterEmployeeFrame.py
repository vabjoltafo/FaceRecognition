from tkinter import messagebox as tkMessageBox, Label, StringVar, Entry, Button, Frame, messagebox
from tkinter.ttk import Combobox

import PIL.Image
import PIL.ImageTk

from Enums import Gender
from FacialRecognition.datasetcreator import createEmployee
from Repositories.EmployeeRepository import getTheIdOfEmployee
from Utilities.DateEntry import DateEntry


class RegisterEmployeeFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.tittleLabel = Label(self, text="Shto Punonjës", font=("Sans-Serif", 25, 'bold')).place(x=5, y=20)

        self.NAME = StringVar()
        self.SURNAME = StringVar()
        self.POSITION = StringVar()
        self.PHONE = StringVar()
        self.EMAIL = StringVar()

        self.nameLabel = Label(self, text='Emri', font=('Sans-Serif',15, 'bold')).place(x=130, y=110)
        self.nameField = Entry(self, width=45, textvariable=self.NAME).place(x=250, y=110, height=25)

        self.surnameLabel = Label(self, text='Mbiemri', font=('Sans-Serif', 15, 'bold')).place(x=130, y=160)
        self.surnameField = Entry(self, width=45, textvariable=self.SURNAME).place(x=250, y=160, height=25)

        self.genderLabel = Label(self, text='Gjinia', font=('Sans-Serif', 15, 'bold')).place(x=130, y=210)
        self.genderCombo = Combobox(self, width=42, values= Gender.genderList)
        self.genderCombo.place(x=250, y=210, height=25)


        self.dateLabel = Label(self, text='Datëlindja', font=('Sans-Serif', 15, 'bold')).place(x=130, y=260)
        self.ageEntry = DateEntry(self, width=42, date_pattern = 'dd/mm/yyyy')
        self.ageEntry._set_text("")
        self.ageEntry.place(x=250, y=260, height=25)

        self.positionLabel = Label(self, text = 'Pozicioni', font=('Sans-Serif', 15, 'bold')).place(x=130, y=310)
        self.positionField = Entry(self, width=45, textvariable=self.POSITION).place(x=250, y=310, height=25)

        self.phoneLabel = Label(self, text = 'Telefoni', font=('Sans-Serif', 15, 'bold')).place(x=130, y=360)
        self.phoneField = Entry(self, width=45, textvariable=self.PHONE).place(x=250, y=360, height=25)

        self.emailLabel = Label(self, text =" Email", font=('Sans-Serif', 15, 'bold')).place(x=130, y=410)
        self.emailField = Entry(self, width=45, textvariable=self.EMAIL).place(x=250, y=410, height=25)

        ShtoImage = PIL.Image.open("Layout\\images\\ShtoButton.png")
        ShtoImage = ShtoImage.resize((700, 450), PIL.Image.ANTIALIAS)
        self.ShtoImage = PIL.ImageTk.PhotoImage(ShtoImage)

        self.insertButton = Button(self, width=90, bd=0, height=43, image = self.ShtoImage,
                                   command=self.insertStudent).place(x=340, y=460)


    def insertStudent(self):

        if self.NAME.get() is '' or self.SURNAME is '':
            tkMessageBox.showwarning('Mesazh', 'Plotësoni fushat Emër apo Mbiemër!')
            
        else:

            id = getTheIdOfEmployee(self.NAME.get(), self.SURNAME.get())

            if id:

                tkMessageBox.showerror('Gabim!', 'Punonjësi me këto të dhëna ekziston!')
            else:
                print("OK!")
                createEmployee(self.NAME.get(), self.SURNAME.get(), self.genderCombo.get(),
                               self.ageEntry.get(), self.POSITION.get(), self.PHONE.get(), self.EMAIL.get())

                messagebox.showinfo("Nevojitet përditësimi i të dhënave!",
                                    "Për të përditësuar të dhënat, shkoni në Konfigurime >> Trajno të dhënat")

