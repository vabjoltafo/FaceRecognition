import os
import shutil
from tkinter import Frame, Label, Entry, Button, messagebox, Toplevel, StringVar, ttk

import PIL.Image
import PIL.ImageTk

from Enums import Gender
from Layout.Frames.EmployeeFrames.TableFrame import TableFrame
from Repositories.EmployeeRepository import getTheInfomationFromEmployees, getEmployeesByName, deleteEmployee, \
    getEmployeeById, updateEmployee, getTheIdOfEmployee
from Utilities.DateEntry import DateEntry
from Utilities.DbUtility import filterData
from Utilities.ExcelExporter import exportEmployeeData
from Utilities.PlaceHolderEntry import PlaceholderEntry


class CrudEmployeeFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.data= getTheInfomationFromEmployees()
        self.nameLabel = Label(self, text="Punonjësit ", font=("Sans-Serif", 25, 'bold'))
        self.nameLabel.place(x=5, y=20)

        self.entry = PlaceholderEntry(self, "Filtro sipas emrit")
        self.entry.place(x=5, y=123)

        KerkoImage = PIL.Image.open("Layout\\images\\KerkoButton.png")
        KerkoImage = KerkoImage.resize((450, 325), PIL.Image.ANTIALIAS)
        self.KerkoPic = PIL.ImageTk.PhotoImage(KerkoImage)

        self.searchButton = Button(self, width=50, height=30, bd=0,
                                   image=self.KerkoPic, command=self.search).place(x=140, y=117)

        EleminoImage = PIL.Image.open("Layout\\images\\EleminoButton.png")
        EleminoImage = EleminoImage.resize((400, 320), PIL.Image.ANTIALIAS)
        self.EleminoImage = PIL.ImageTk.PhotoImage(EleminoImage)

        self.deleteButton = Button(self, width=70, height=30, bd=0, image=self.EleminoImage,
                                   command=self.deleteEmployee).place(x=205, y=117)

        NdryshoImage = PIL.Image.open("Layout\\images\\NdryshoButton.png")
        NdryshoImage = NdryshoImage.resize((400, 320), PIL.Image.ANTIALIAS)
        self.NdryshoImage = PIL.ImageTk.PhotoImage(NdryshoImage)
        self.editButton = Button(self, width=80, height=30, bd=0, image=self.NdryshoImage,
                                 command=self.editEmployee).place(x=287, y=117)

        EksportoImage = PIL.Image.open("Layout\\images\\EksportoButton.png")
        EksportoImage = EksportoImage.resize((400, 390), PIL.Image.ANTIALIAS)
        self.EksportoImage = PIL.ImageTk.PhotoImage(EksportoImage)
        self.exportToExcel = Button(self, height=30, width=143,
                                    bd=0, image=self.EksportoImage, command=self.exportToExcel).place(x=380, y=116)

        self.table = TableFrame(self)
        self.table.place(x=200, y=140)


    def search(self):
        self.data = ()
        if self.entry.get() is 'Filtro sipas emrit' or self.entry.get() is ' ' or self.entry.get() is '' or self.entry.get() is None:
            self.data = getTheInfomationFromEmployees()
        else:
            self.data = filterData(self.entry.get(), getTheInfomationFromEmployees())
        self.table = TableFrame(self)
        self.table.place(x=200, y=140)
        self.table.updateTable(self.data)


    def deleteEmployee(self):
        if self.table.getResponse() is ():
            messagebox.showerror('Kujdes!', 'Zgjidhni një punonjës në tabelë!')
        else:
            index = int(self.table.getResponse()[1])
            data = self.table.getData()
            id = data[index][0]

            MsgBox = messagebox.askquestion('Fshirje', 'Jeni i sigurt që doni të fshini punonjësin '
                                            + data[index][1] + ' ' + data[index][2] + '?',
                                            icon='warning')

            if MsgBox == 'yes':
                path = ".//Image_DataSet//"
                part = data[index][1] + ' ' + data[index][2]
                try:
                    shutil.rmtree(path + str(part))
                except OSError as ex:
                    print(ex)

                deleteEmployee(id)
                data = getTheInfomationFromEmployees()
                # self.table = TableFrame(self)
                # self.table.place(x=200, y=140)
                self.table.updateTable(data)
                messagebox.showinfo("Nevojitet përditësimi i të dhënave!",
                                    "Për të përditësuar të dhënat, shkoni në Konfigurime >> Trajno të dhënat")

    def editEmployee(self):

        if self.table.getResponse() is ():

            messagebox.showerror('Kujdes!', 'Zgjidhni një punonjes në tabelë!')

        else:
            index = int(self.table.getResponse()[1])
            tuple = self.table.getData()
            id = tuple[index][0]
            self.data = getEmployeeById(id)
            self.width = 500
            self.height = 500
            self.toplevel_dialog = Toplevel(self)
            self.toplevel_dialog.minsize(self.width, self.height)
            # self.toplevel_dialog.wm_overrideredirect(True)
            self.screen_width = self.toplevel_dialog.winfo_screenwidth()
            self.screen_height = self.toplevel_dialog.winfo_screenheight()
            self.x = (self.screen_width / 2) - (self.width / 2)
            self.y = (self.screen_height / 2) - (self.height / 2)
            self.toplevel_dialog.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
            self.toplevel_dialog.transient(self)
            self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)

            self.toplevel_dialog_label = Label(self.toplevel_dialog, text='Ndrysho të dhënat e punonjësit', font=("Sans-Serif", 15,'bold'))
            self.toplevel_dialog_label.place(x=100, y=5)

            self.NAME = StringVar()
            self.SURNAME = StringVar()
            self.POSITION = StringVar()
            self.PHONE = StringVar()
            self.EMAIL = StringVar()
            self.GENDER = StringVar()
            self.DATE = StringVar()


            self.NAME.set(self.data[1])
            self.oldName=self.data[1]
            self.SURNAME.set(self.data[2])
            self.oldSurname=self.data[2]
            self.POSITION.set(self.data[3])
            self.DATE.set(self.data[4].strftime("%m/%d/%Y"))
            self.PHONE.set(self.data[5])
            self.EMAIL.set(self.data[6])
            self.GENDER.set(self.data[7])


            self.nameLabel = Label(self.toplevel_dialog, text='Emri', font=('Sans-Serif', 15, 'bold')).place(x=40, y=70)
            self.nameField = Entry(self.toplevel_dialog, width=45, textvariable=self.NAME)
            self.nameField.place(x=160, y=70, height=25)


            self.surnameLabel = Label(self.toplevel_dialog, text='Mbiemri', font=('Sans-Serif', 15, 'bold')).place(x=40, y=120)
            self.surnameField = Entry(self.toplevel_dialog, width=45, textvariable=self.SURNAME)
            self.surnameField.place(x=160, y=120, height=25)

            self.genderLabel = Label(self.toplevel_dialog, text='Gjinia', font=('Sans-Serif', 15, 'bold')).place(x=40, y=170)
            self.genderCombo = ttk.Combobox(self.toplevel_dialog, width=42, values=Gender.genderList, textvariable=self.GENDER)
            self.genderCombo.place(x=160, y=170, height=25)

            self.dateLabel = Label(self.toplevel_dialog, text='Datëlindja', font=('Sans-Serif', 15, 'bold')).place(x=40, y=220)
            self.ageEntry = DateEntry(self.toplevel_dialog, width=42, date_pattern='dd/mm/yyyy', textvariable=self.DATE)
            self.ageEntry.place(x=160, y=220, height=25)

            self.positionLabel = Label(self.toplevel_dialog, text='Pozicioni', font=('Sans-Serif', 15, 'bold')).place(x=40, y=270)
            self.positionField = Entry(self.toplevel_dialog, width=45, textvariable=self.POSITION).place(x=160, y=270, height=25)

            self.phoneLabel = Label(self.toplevel_dialog, text='Telefoni', font=('Sans-Serif', 15, 'bold')).place(x=40, y=320)
            self.phoneField = Entry(self.toplevel_dialog, width=45, textvariable=self.PHONE).place(x=160, y=320, height=25)

            self.emailLabel = Label(self.toplevel_dialog, text=" Email", font=('Sans-Serif', 15, 'bold')).place(x=40, y=370)
            self.emailField = Entry(self.toplevel_dialog, width=45, textvariable=self.EMAIL).place(x=160, y=370, height=25)

            RuajImage = PIL.Image.open("Layout\\images\\RuajButton.png")
            RuajImage = RuajImage.resize((450, 300), PIL.Image.ANTIALIAS)
            self.RuajImage = PIL.ImageTk.PhotoImage(RuajImage)

            self.toplevel_dialog_yes_button = Button(self.toplevel_dialog, image=self.RuajImage, bd=0, width=55, height=45,
                                                     command=self.updateAndClose)
            self.toplevel_dialog_yes_button.place(x=190, y=450)

            AnuloImage = PIL.Image.open("Layout\\images\\AnuloButton.png")
            AnuloImage = AnuloImage.resize((400, 300), PIL.Image.ANTIALIAS)
            self.AnuloImage = PIL.ImageTk.PhotoImage(AnuloImage)

            self.toplevel_dialog_no_button = Button(self.toplevel_dialog, bd=0, height=45, width=55, image=self.AnuloImage, command=self.Close_Toplevel)
            self.toplevel_dialog_no_button.place(x=250, y=450)


    def updateAndClose(self):
        if self.oldName == self.NAME.get() and self.oldSurname == self.SURNAME.get():
            updateEmployee(self.data[0], self.NAME.get(), self.SURNAME.get(), self.GENDER.get(), self.ageEntry.get(),
                           self.POSITION.get(), self.PHONE.get(), self.EMAIL.get())

            data = getTheInfomationFromEmployees()
            self.table = TableFrame(self)
            self.table.place(x=200, y=140)
            self.table.updateTable(data)
            self.toplevel_dialog.destroy()
            messagebox.showinfo("Nevojitet përditësimi i të dhënave!",
                                "Për të përditësuar të dhënat, shkoni në Konfigurime >> Trajno të dhënat")

        else:
            if not getTheIdOfEmployee(self.NAME.get(), self.SURNAME.get()):
                try:
                    os.rename('.//Image_DataSet//'+self.oldName + ' ' + self.oldSurname, './/Image_DataSet//'+self.NAME.get() + ' ' + self.SURNAME.get())
                except OSError as ex:
                    print(ex)

                updateEmployee(self.data[0], self.NAME.get(), self.SURNAME.get(), self.GENDER.get(), self.ageEntry.get(),
                               self.POSITION.get(), self.PHONE.get(), self.EMAIL.get())

                data = getTheInfomationFromEmployees()
                # self.table = TableFrame(self)
                # self.table.place(x=200, y=140)
                self.table.updateTable(data)
                self.toplevel_dialog.destroy()
                messagebox.showinfo("Nevojitet përditësimi i të dhënave!",
                                    "Për të përditësuar të dhënat, shkoni në Konfigurime >> Trajno të dhënat")
            else:
                messagebox.showerror("Gabim!", "Ky punonjës ekziston në databazë!")

    def Close_Toplevel(self):
        self.toplevel_dialog.destroy()

    def exportToExcel(self):
        exportEmployeeData(self.data)