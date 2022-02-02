from tkinter import Frame, Label, Button, messagebox, Toplevel, Entry, StringVar
from tkinter.ttk import Combobox

import PIL

from Enums import Years, Months
from Layout.Frames.RaporteFrames.EmployeeSalaryTable import EmployeeSalaryTable
from Repositories.EmployeeRepository import getTheHoursOfEmployeesByMonth, getAllEmployeeNameAndSurname
from Utilities.Convertors import getEmployeeFullNameList
from Utilities.DbUtility import getDataForEmployeeSalary
from Utilities.ExcelExporter import exportEmployeHours


class EmployeeSalaryFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.tittleLabel = Label(self, text="Orët e punonjësve", font=("Sans-Serif", 25, 'bold')).place(x=5, y=20)

        self.comboLabel = Label(self, text='Punonjësit', font=("Sans-Serif", 12, 'bold'))
        self.comboLabel.place(x=5, y=98)
        listOfEmployees = getEmployeeFullNameList(getAllEmployeeNameAndSurname())
        self.entryEmployee = Combobox(self, width=16, value=listOfEmployees, font="Sans-Serif 10")
        self.entryEmployee.place(x=5, y=123)


        self.comboLabel = Label(self, text='Viti', font=("Sans-Serif", 12, 'bold'))
        self.comboLabel.place(x=150, y=98)
        listOFYears = Years.values
        self.entryYears = Combobox(self, width=10, value=listOFYears, font="Sans-Serif 10")
        self.entryYears.place(x=150, y=123)


        self.comboLabel = Label(self, text='Muaji', font=("Sans-Serif", 12, 'bold'))
        self.comboLabel.place(x=255, y=98)
        listOFMonths = Months.values
        self.entryMonths = Combobox(self, width=10, value=listOFMonths, font="Sans-Serif 10")
        self.entryMonths.place(x=255, y=123)

        PastroImage = PIL.Image.open("Layout\\images\\PastroButton.png")
        PastroImage = PastroImage.resize((400, 330), PIL.Image.ANTIALIAS)
        self.PastroImage = PIL.ImageTk.PhotoImage(PastroImage)
        self.clearButton = Button(self, width=50, height=25, bd=0, image=self.PastroImage,
                                  command=self.clearFields).place(x=423, y=120)


        KerkoImage = PIL.Image.open("Layout\\images\\KerkoButton.png")
        KerkoImage = KerkoImage.resize((450, 320), PIL.Image.ANTIALIAS)
        self.KerkoPic = PIL.ImageTk.PhotoImage(KerkoImage)
        self.searchButton = Button(self, width=55, height=25, bd=0,
                                   image=self.KerkoPic, command=self.search).place(x=360, y=120)


        EksportoImage = PIL.Image.open("Layout\\images\\EksportoButton.png")
        EksportoImage = EksportoImage.resize((400, 390), PIL.Image.ANTIALIAS)
        self.EksportoImage = PIL.ImageTk.PhotoImage(EksportoImage)
        self.exportToExcel = Button(self, height=30, width=143,
                                    bd=0, image=self.EksportoImage, command=self.exportHours).place(x=485, y=117)

        llogaritImage = PIL.Image.open("Layout\\images\\LlogaritButton.png")
        llogaritImage = llogaritImage.resize((400,320), PIL.Image.ANTIALIAS)
        self.llogaritImage = PIL.ImageTk.PhotoImage(llogaritImage)

        self.llogaritButton = Button(self, width=100, height=30, bd=0, image = self.llogaritImage,
                                     command=self.openSalaryModal).place(x=642, y=116)


        self.table = EmployeeSalaryTable(self)
        self.table.place(x=200, y=145)


    def search(self):
        employeeName = self.entryEmployee.get()
        year = self.entryYears.get()
        month = self.entryMonths.get()

        if len(employeeName) is 0:
            messagebox.showerror("Kujdes!", "Zgjidhni punonjësin!")
        else:
            if len(year) is 0:
                messagebox.showerror("Kujdes!", "Zgjidhni vitin!")
            else:
                if len(month) is 0:
                    messagebox.showerror("Kujdes!", "Zgjidhni muajin!")
                else:
                    int_month = Months.MONTHS_DICT[month]
                    data = getTheHoursOfEmployeesByMonth(employeeName, float(year), float(int_month))
                    getDataForEmployeeSalary(employeeName, data)
                    self.table.updateTable(data)


    def openSalaryModal(self):
        employeeName = self.entryEmployee.get()
        year = self.entryYears.get()
        month = self.entryMonths.get()

        if len(employeeName) is 0 or len(year) is 0 or len(month) is 0:
            messagebox.showerror("Kujdes", "Te gjitha fushat duhet te jene te plotesuara")
        else:
            int_month = Months.MONTHS_DICT[month]
            data = getDataForEmployeeSalary(employeeName, getTheHoursOfEmployeesByMonth(employeeName, float(year), float(int_month)))
            self.width = 620
            self.height = 450

            ORET = StringVar()
            PAGA_ORARE = StringVar()
            PAGA_BRUTO = StringVar()
            KONTRIB_SHENDETSORE = StringVar()
            KONTRIB_SHOQERORE = StringVar()
            TAP1 = StringVar()
            TAP2 = StringVar()
            TAP3 = StringVar()
            PAGA_NETO = StringVar()

            ORET.set(data[0])
            PAGA_ORARE.set(data[1])
            PAGA_BRUTO.set(data[2])
            KONTRIB_SHOQERORE.set(data[3])
            KONTRIB_SHENDETSORE.set(data[4])
            TAP1.set(data[5])
            TAP2.set(data[6])
            TAP3.set(data[7])
            PAGA_NETO.set(data[8])

            self.toplevel_dialog = Toplevel(self)
            self.toplevel_dialog.minsize(self.width, self.height)
            self.screen_width = self.toplevel_dialog.winfo_screenwidth()
            self.screen_height = self.toplevel_dialog.winfo_screenheight()
            self.x = (self.screen_width / 2) - (self.width / 2)
            self.y = (self.screen_height / 2) - (self.height / 2)
            self.toplevel_dialog.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
            self.toplevel_dialog.transient(self)
            self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)
            self.toplevel_dialog_label = Label(self.toplevel_dialog, text='Paga e punonjësit ' + self.entryEmployee.get(),
                                               font=("Sans-Serif", 15, 'bold')).pack()

            self.oretLabel = Label(self.toplevel_dialog, text='Orët', font=('Sans-Serif', 13, 'bold')).place(x=20, y=70)
            self.oretEntry = Entry(self.toplevel_dialog, width=45, state='disabled', textvariable=ORET, justify='center').place(x=330, y=70, height=25)

            self.pagaorareLabel = Label(self.toplevel_dialog, text='Paga orare ose lekë/orë', font=('Sans-Serif', 13, 'bold')).place(x=20, y=100)
            self.pagaorareEntry = Entry(self.toplevel_dialog, width=45, state='disabled',textvariable=PAGA_ORARE, justify='center').place(x=330, y=100, height=25)

            self.pagabrutoLabel = Label(self.toplevel_dialog, text='Paga Bruto', font=('Sans-Serif', 13, 'bold')).place(x=20, y=130)
            self.pagabrutoEntry = Entry(self.toplevel_dialog, width=45, state='disabled', textvariable=PAGA_BRUTO, justify='center').place(x=330, y=130, height=25)

            self.sigurimshoqerorLabel = Label(self.toplevel_dialog, text='Kontributet e sigurimit shoqëror',
                                              font=('Sans-Serif', 13, 'bold')).place(x=20, y=160)
            self.sigurimshoqerorEntry = Entry(self.toplevel_dialog, width=45, state='disabled',
                                              textvariable=KONTRIB_SHOQERORE, justify='center').place(x=330, y=160, height=25)

            self.sigurimishendetesorLabel = self.sigurimishendetesorLabel = Label(self.toplevel_dialog, text='Kontributet e sigurimit shëndetësor',
                                                 font=('Sans-Serif', 13, 'bold')).place(x=20, y=190)
            self.sigurimishendetesorEntry = Entry(self.toplevel_dialog, width=45, state='disabled', textvariable=KONTRIB_SHENDETSORE,
                                                  justify='center').place(x=330, y=190, height=25)

            self.Tap0Label = Label(self.toplevel_dialog, text='TAP 0 - 30000 lekë',
                                                 font=('Sans-Serif', 13, 'bold')).place(x=20, y=220)
            self.Tap0Entry = Entry(self.toplevel_dialog, width=45, state='disabled', textvariable=TAP1, justify='center').place(x=330, y=220, height=25)

            self.Tap1Label = Label(self.toplevel_dialog, text='TAP 30000 - 150000 lekë',
                                                 font=('Sans-Serif', 13, 'bold')).place(x=20, y=250)
            self.Tap1Entry = Entry(self.toplevel_dialog, width=45, state='disabled',textvariable=TAP2, justify='center').place(x=330, y=250, height=25)

            self.Tap2Label = Label(self.toplevel_dialog, text='TAP mbi 150000 lekë',
                                                 font=('Sans-Serif', 13, 'bold')).place(x=20, y=280)
            self.Tap2Entry = Entry(self.toplevel_dialog, width=45, state='disabled', textvariable=TAP3, justify='center').place(x=330, y=280, height=25)

            self.frame = Frame(self.toplevel_dialog,width=583, height=2, highlightbackground="black",highlightthickness = 1, bd=1).place(x=20, y=308)

            self.paganetoLabel = Label(self.toplevel_dialog, text='Paga Neto', font=('Sans-Serif', 13, 'bold')).place(x=20, y=310)
            self.paganetoLabelValue = Label(self.toplevel_dialog, width=45,  font=('Sans-Serif', 10, 'normal'), textvariable=PAGA_NETO, justify='center').place(x=290, y=310, height=25)

            MbyllImage = PIL.Image.open("Layout\\images\\MbyllButton.png")
            MbyllImage = MbyllImage.resize((550, 350), PIL.Image.ANTIALIAS)
            self.MbyllImage = PIL.ImageTk.PhotoImage(MbyllImage)

            self.toplevel_dialog_no_button = Button(self.toplevel_dialog, bd=0, height=30, width=65, image=self.MbyllImage,
                                                    command=self.Close_Toplevel)
            self.toplevel_dialog_no_button.place(x=270, y=400)


    def Close_Toplevel(self):
        self.toplevel_dialog.destroy()


    def clearFields(self):
        self.entryEmployee.set('')
        self.entryMonths.set('')
        self.entryYears.set('')

    def exportHours(self):
        exportEmployeHours(self.table.getData())