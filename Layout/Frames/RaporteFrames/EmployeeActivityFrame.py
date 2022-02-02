from tkinter import Frame, Label, Button
from tkinter.ttk import Combobox
import PIL
from Layout.Frames.RaporteFrames.ActivityEmployeeTable import ActivityEmployeeTable
from Repositories.EmployeeRepository import getActivityOfEmployees, getAllEmployeeNameAndSurname, \
    getActivityOfEmployeesByDate, getActivityOfEmployeesByName, getActivityOfEmployeesByNameAndDate
from Utilities.Convertors import getEmployeeFullNameList, editListOfActivities
from Utilities.DateEntry import DateEntry
from Utilities.ExcelExporter import exportEmployeeActivityData


class EmployeeActivityFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.data = editListOfActivities(getActivityOfEmployees())
        self.tittleLabel = Label(self, text="Aktiviteti i punonjësve", font=("Sans-Serif", 25, 'bold')).place(x=5, y=20)

        self.comboLabel = Label(self, text = 'Punonjësit', font=("Sans-Serif", 12, 'bold'))
        self.comboLabel.place(x=5, y=98)
        listOfEmployees = getEmployeeFullNameList(getAllEmployeeNameAndSurname())
        self.entry = Combobox(self, width=16, value=listOfEmployees, font="Sans-Serif 10")
        self.entry.place(x=5, y=123)


        self.dateLabel = Label(self, text='Data', font=("Sans-Serif", 12, 'bold'))
        self.dateLabel.place(x=145, y=98)
        self.dateEntry = DateEntry(self, width=16, date_pattern='dd/mm/yyyy', font="Sans-Serif 10")
        self.dateEntry._set_text("")
        self.dateEntry.place(x=145, y=123)

        PastroImage = PIL.Image.open("Layout\\images\\PastroButton.png")
        PastroImage = PastroImage.resize((400, 320), PIL.Image.ANTIALIAS)
        self.PastroImage = PIL.ImageTk.PhotoImage(PastroImage)

        self.clearButton = Button(self, width=50, height=25, bd=0, image=self.PastroImage,
                                    command=self.clearFields).place(x=290, y=120)


        KerkoImage = PIL.Image.open("Layout\\images\\KerkoButton.png")
        KerkoImage = KerkoImage.resize((450, 320), PIL.Image.ANTIALIAS)
        self.KerkoPic = PIL.ImageTk.PhotoImage(KerkoImage)
        self.searchButton = Button(self, width=55, height=25, bd=0,
                                   image=self.KerkoPic, command=self.search).place(x=350, y=120)


        EksportoImage = PIL.Image.open("Layout\\images\\EksportoButton.png")
        EksportoImage = EksportoImage.resize((400, 390), PIL.Image.ANTIALIAS)
        self.EksportoImage = PIL.ImageTk.PhotoImage(EksportoImage)
        self.exportToExcel = Button(self, height =30, width = 143,
                                    bd=0, image = self.EksportoImage, command=self.exportToExcel).place(x=415, y=117)


        self.table = ActivityEmployeeTable(self)
        self.table.place(x=200, y=140)

    def search(self):
        self.data = ()
        name = self.entry.get()
        date = self.dateEntry.get()

        if len(name) is 0 and len(date) is 0:
            self.data = getActivityOfEmployees()
            # print('1',self.entry.get(),'-', self.dateEntry.get())

        elif len(str(name)) is 0 and len(str(date)) is not 0:
            self.data = getActivityOfEmployeesByDate(date)
            # print('2', self.entry.get(),'-', self.dateEntry.get())

        elif len(str(name)) is not 0 and len(str(date)) is 0:
            self.data = getActivityOfEmployeesByName(name)
            # print('3', self.entry.get(),'-', self.dateEntry.get())

        elif len(name) is not 0 and len(date) is not 0:
            self.data = getActivityOfEmployeesByNameAndDate(name, date)
            # print('4', self.entry.get(),'-', self.dateEntry.get())

        editedData = editListOfActivities(self.data)
        # self.table = ActivityEmployeeTable(self)
        self.table.updateTable(editedData)
        # self.table.place(x=200, y=140)

    def clearFields(self):
        # print('before', len(self.entry.get()), len(self.dateEntry.get()))
        self.entry.select_clear()
        self.entry.set('')
        self.dateEntry._set_text("")
        # print('after', len(self.entry.get()), len(self.dateEntry.get()))


    def exportToExcel(self):
        exportEmployeeActivityData(self.data)

