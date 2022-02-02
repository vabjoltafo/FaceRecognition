from tkinter import Frame
from tkinter import ttk
from Layout.Frames.EmployeeFrames.CrudEmployeeFrame import CrudEmployeeFrame
from Layout.Frames.EmployeeFrames.RegisterEmployeeFrame import RegisterEmployeeFrame


class EmployeeFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)

        tabControl = ttk.Notebook(self, width = 750, height = 600)

        self.tab1 = CrudEmployeeFrame(tabControl)
        tabControl.add(self.tab1, text="Punonjësit")

        tab2 = RegisterEmployeeFrame(tabControl)
        tabControl.add(tab2, text="Shto punonjës")
        tabControl.pack(expand=1, fill="both")



