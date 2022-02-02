from tkinter import Frame, Label, Button, Toplevel, Entry, StringVar, messagebox, Checkbutton, IntVar
from tkinter.ttk import Combobox
from Repositories.EmployeeRepository import getTheHoursOfEmployeesByMonth, getAllEmployeeNameAndSurname, getFullNameById
from Repositories.WageEmployeeRepository import selectWageByEmployeeId, insertWageOfEmployee, selectDataToDisplay, \
    selectWageById, updateWage, deleteWage
from Utilities.Convertors import getEmployeeFullNameList
import PIL
from Layout.Frames.KonfigurimeFrames.WageTableFrame import WageTableFrame
from Utilities.DbUtility import isANumber, filterData
from Utilities.ExcelExporter import exportEmployeWage
from Utilities.PlaceHolderEntry import PlaceholderEntry


class WageEmployeeFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.nameLabel = Label(self, text="Paga orare e punonjësve ", font=("Sans-Serif", 25, 'bold'))
        self.nameLabel.place(x=5, y=20)


        self.entry = PlaceholderEntry(self, "Filtro sipas emrit")
        self.entry.place(x=5, y=123)

        KerkoImage = PIL.Image.open("Layout\\images\\KerkoButton.png")
        KerkoImage = KerkoImage.resize((450, 320), PIL.Image.ANTIALIAS)
        self.KerkoPic = PIL.ImageTk.PhotoImage(KerkoImage)

        self.searchButton = Button(self, width=50, height=30, bd=0,
                                   image=self.KerkoPic, command=self.search).place(x=140, y=117)


        EksportoImage = PIL.Image.open("Layout\\images\\EksportoButton.png")
        EksportoImage = EksportoImage.resize((400, 390), PIL.Image.ANTIALIAS)
        self.EksportoImage = PIL.ImageTk.PhotoImage(EksportoImage)
        self.exportToExcel = Button(self, height=30, width=143,
                                    bd=0, image=self.EksportoImage, command=self.exportToExcel).place(x=260, y=115)

        ShtoImage = PIL.Image.open("Layout\\images\\ShtoButton.png")
        ShtoImage = ShtoImage.resize((400, 350), PIL.Image.ANTIALIAS)
        self.ShtoImage = PIL.ImageTk.PhotoImage(ShtoImage)

        self.insertButton = Button(self, width=50, bd=0, height=40, image=self.ShtoImage,
                                   command=self.openAddForm).place(x=200, y=108)


        self.table = WageTableFrame(self)
        self.table.place(x=200, y=140)
        self.var1 = IntVar()

    def openAddForm(self):
        self.width = 400
        self.height = 220
        self.toplevel_dialog = Toplevel(self)
        self.toplevel_dialog.minsize(self.width, self.height)
        self.screen_width = self.toplevel_dialog.winfo_screenwidth()
        self.screen_height = self.toplevel_dialog.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.toplevel_dialog.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.toplevel_dialog.transient(self)
        self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)

        self.toplevel_dialog_label = Label(self.toplevel_dialog, text='Shto',
                                           font=("Sans-Serif", 15, 'bold')).pack()
        self.FULL_NAME = StringVar()
        self.WAGE = StringVar()

        listOfEmployees = getEmployeeFullNameList(getAllEmployeeNameAndSurname())
        self.punonjesiLabel = Label(self.toplevel_dialog, text='Punonjësi', font=('Sans-Serif', 13, 'bold')).place(x=20, y=50)
        self.punonjesiEntry = Combobox(self.toplevel_dialog, width=16, value=listOfEmployees, textvariable=self.FULL_NAME, font=('Sans-Serif', 13)).place(x=170, y=50)

        self.pagaorareLabel = Label(self.toplevel_dialog, text='Paga orare', font=('Sans-Serif', 13, 'bold')).place(x=20, y=90)
        self.pagaorareEntry = Entry(self.toplevel_dialog, width=27, textvariable=self.WAGE).place(x=170, y=90, height=25)

        self.orare = Checkbutton(self.toplevel_dialog, text='Orar', onvalue=1, offvalue=0, variable=self.var1)
        self.orare.place(x=190, y=120)



        RuajImage = PIL.Image.open("Layout\\images\\RuajButton.png")
        RuajImage = RuajImage.resize((450, 300), PIL.Image.ANTIALIAS)
        self.RuajImage = PIL.ImageTk.PhotoImage(RuajImage)
        self.toplevel_dialog_yes_button = Button(self.toplevel_dialog, image=self.RuajImage, bd=0, width=55,
                                                 height=45, command=self.insertWage)

        self.toplevel_dialog_yes_button.place(x=170, y=180)

        AnuloImage = PIL.Image.open("Layout\\images\\AnuloButton.png")
        AnuloImage = AnuloImage.resize((400, 300), PIL.Image.ANTIALIAS)
        self.AnuloImage = PIL.ImageTk.PhotoImage(AnuloImage)

        self.toplevel_dialog_no_button = Button(self.toplevel_dialog, bd=0, height=45, width=55,
                                                image=self.AnuloImage, command=self.Close_Toplevel)

        self.toplevel_dialog_no_button.place(x=260, y=2080)

    def Close_Toplevel(self):
        self.toplevel_dialog.destroy()


    def insertWage(self):
        if len(self.FULL_NAME.get()) is 0:
            messagebox.showerror("Kujdes", "Zgjidhni punonjesin!")
        else:
            try:
                num = float(self.WAGE.get())
                if selectWageByEmployeeId(self.FULL_NAME.get()):
                    messagebox.showerror("Kujdes", "Punonjesi aktualisht ka pagen orare")
                else:
                    insertWageOfEmployee(self.FULL_NAME.get(), self.WAGE.get(), str(self.var1.get()))
                    data = selectDataToDisplay()
                    self.table = WageTableFrame(self)
                    self.table.place(x=200, y=140)
                    self.table.updateTable(data)
                    self.Close_Toplevel()
            except ValueError:
                messagebox.showerror("Kujdes", "Paga orare duhet te jete nje numer")


    def updateWage(self):
        if len(self.WAGE1.get()) is 0:
            messagebox.showerror("Kujdes", "Paga s'mund te jete bosh!")
        else:
             if isANumber(self.WAGE1.get()):
                 updateWage(self.data[0], self.WAGE1.get(), self.orare.getboolean())
                 data = selectDataToDisplay()
                 self.table = WageTableFrame(self)
                 self.table.place(x=200, y=140)
                 self.table.updateTable(data)
                 self.Close_Toplevel()
             else:
                 messagebox.showerror("Kujdes", "Paga duhet te jete nje numer!")


    def deleteWage(self):
        if self.table.getResponse() is ():
            messagebox.showerror('Kujdes!', 'Zgjidhni një punonjes në tabelë!')
        else:
            index = int(self.table.getResponse()[1])
            tuple = self.table.getData()
            wageId = selectWageByEmployeeId(tuple[index][0] + " " + tuple[index][1])[0]
            print(wageId)
            MsgBox = messagebox.askquestion('Fshirje', 'Jeni i sigurt që doni të fshini punonjesin '
                                            + tuple[index][0] + ' ' + tuple[index][1] + '?',
                                            icon='warning')
            if MsgBox == 'yes':
                deleteWage(wageId)
                data = selectDataToDisplay()
                self.table = WageTableFrame(self)
                self.table.place(x=200, y=140)
                self.table.updateTable(data)


    def search(self):
        data = filterData(self.entry.get(), selectDataToDisplay())
        self.table.updateTable(data)

    def exportToExcel(self):
        exportEmployeWage(self.table.getData())



