from tkinter import Frame, ttk

from Layout.Frames.RaporteFrames.AllEmployeesSalaryFrame import AllEmployeeSalaryFrame
from Layout.Frames.RaporteFrames.EmployeeActivityFrame import EmployeeActivityFrame
from Layout.Frames.RaporteFrames.EmployeeSalaryFrame import EmployeeSalaryFrame


class RaporteFrame(Frame):

    def __init__(self,root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600

        tabControl = ttk.Notebook(self, width=750, height=600)

        self.employeeActivity = EmployeeActivityFrame(self)
        tabControl.add(self.employeeActivity, text='Hyrjet/Daljet e punonjësve')

        self.employeeSalary = EmployeeSalaryFrame(self)
        tabControl.add(self.employeeSalary, text='Oret e punonjësve')

        self.allEmployeeSalary = AllEmployeeSalaryFrame(self)
        tabControl.add(self.allEmployeeSalary, text='Pagat e punonjësve')

        tabControl.pack(expand=1, fill="both")





