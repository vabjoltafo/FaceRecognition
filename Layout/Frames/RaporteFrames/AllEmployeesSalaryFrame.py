from tkinter import Frame, Label, Button, messagebox
from tkinter.ttk import Combobox
import PIL
from Enums import Years, Months
from Layout.Frames.RaporteFrames.AllEmployeeSalaryTable import AllEmployeeSalaryTable
from Utilities.DbUtility import getAllEmployeeSalary


class AllEmployeeSalaryFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600
        self.tittleLabel = Label(self, text="Pagat e punonjësve", font=("Sans-Serif", 25, 'bold')).place(x=5, y=20)

        self.comboLabel = Label(self, text='Viti', font=("Sans-Serif", 12, 'bold'))
        self.comboLabel.place(x=5, y=98)
        listOFYears = Years.values
        self.entryYears = Combobox(self, width=10, value=listOFYears, font="Sans-Serif 10")
        self.entryYears.place(x=5, y=123)

        self.comboLabel = Label(self, text='Muaji', font=("Sans-Serif", 12, 'bold'))
        self.comboLabel.place(x=120, y=98)
        listOFMonths = Months.values
        self.entryMonths = Combobox(self, width=10, value=listOFMonths, font="Sans-Serif 10")
        self.entryMonths.place(x=120, y=123)

        KerkoImage = PIL.Image.open("Layout\\images\\KerkoButton.png")
        KerkoImage = KerkoImage.resize((450, 320), PIL.Image.ANTIALIAS)
        self.KerkoPic = PIL.ImageTk.PhotoImage(KerkoImage)
        self.searchButton = Button(self, width=55, height=25, bd=0,
                                   image=self.KerkoPic, command=self.search).place(x=340, y=120)

        self.table = AllEmployeeSalaryTable(self)
        self.table.place(x=200, y=145)

    def search(self):
        year = self.entryYears.get()
        month = self.entryMonths.get()

        if len(year) is 0 or len(month) is 0:
            messagebox.showerror("Kujdes", "Te gjitha fushat duhet te jene te plotesuara")
        else:
            data = getAllEmployeeSalary(month, year)
            self.table.updateTable(data)