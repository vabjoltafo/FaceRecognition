from tkinter import Frame
from tkinter import ttk

from Layout.Frames.KonfigurimeFrames.DatasetViewerFrame import DatasetViewerFrame
from Layout.Frames.KonfigurimeFrames.SalaryConfigurationFrame import SalaryConfigurationFrame
from Layout.Frames.KonfigurimeFrames.TrainDataFrame import TrainDataFrame
from Layout.Frames.KonfigurimeFrames.WageEmployeeFrame import WageEmployeeFrame


class KonfigurimeFrame(Frame):

    def __init__(self, root):
        Frame.__init__(self)

        tabControl = ttk.Notebook(self, width=750, height=600)

        self.trainFrame = TrainDataFrame(self)
        tabControl.add(self.trainFrame, text='Trajno të dhënat')

        self.salaryConfiguration = SalaryConfigurationFrame(self)
        tabControl.add(self.salaryConfiguration, text='Kontributet dhe Tatimi')

        self.wageEmployee = WageEmployeeFrame(self)
        tabControl.add(self.wageEmployee, text='Paga orare e punonjësve')

        self.viewer = DatasetViewerFrame(self)
        tabControl.add(self.viewer, text='Dataseti i punonjesve')

        tabControl.pack(expand=1, fill="both")

