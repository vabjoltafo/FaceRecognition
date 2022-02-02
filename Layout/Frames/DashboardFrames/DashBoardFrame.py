from tkinter import SUNKEN
from tkinter.ttk import Label, Frame, LabelFrame

from Layout.Frames.DashboardFrames.GenderChartFrame import GenderChartFrame
from Layout.Frames.DashboardFrames.LatestRegisteredEmployeesFrame import LatestRegisteredEmployeesFrame
from Layout.Frames.DashboardFrames.LoggedInEmployeesFrame import LoggedInEmployeesFrame
from Layout.Frames.DashboardFrames.PositionChartFrame import PositionChartFrame
from Layout.Frames.DashboardFrames.TimeLineChartFrame import TimeLineChartFrame


class DashboardFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self)
        self.width = 750
        self.height = 600

        self.nameLabel = Label(text="Dashboard ", font=("Sans-Serif", 25, 'bold'))
        self.nameLabel.place(x=208, y=30)

        self.buildEmployeeGenderChart()
        self.buildEmployeePositionChart()
        self.buildLatestRegisteredEmployees()
        self.buildLoggedInEmployees()
        self.buildTimeLineChart()

    def buildLatestRegisteredEmployees(self):
        self.labelFrame = LabelFrame(text = "Punonjësit e regjistruar së fundmi", width=370, height=180)
        self.table = LatestRegisteredEmployeesFrame(self.labelFrame)
        self.table.place(x=0, y=0)
        self.labelFrame.place(x=201, y=212)


    def buildLoggedInEmployees(self):
        self.loggedInFrame = LabelFrame(text = "Punonjësit e loguar për sot", width=370, height=180)
        self.table2 = LoggedInEmployeesFrame(self.loggedInFrame)
        self.table2.place(x=0, y=0)
        self.loggedInFrame.place(x=578, y=212)


    def buildEmployeeGenderChart(self):
        self.genderFrame = Frame(width=370, height=100)
        self.table3 = GenderChartFrame(self.genderFrame, bd=1, relief=SUNKEN)
        self.table3.place(x=0, y=0)
        self.genderFrame.place(x=201, y=106)

    def buildTimeLineChart(self):
        self.timeLineFrame = Frame(width=370, height=100)
        self.table4 = TimeLineChartFrame(self.timeLineFrame, bd=1, relief=SUNKEN)
        self.table4.place(x=0, y=0)
        self.timeLineFrame.place(x=201, y=399)

    def buildEmployeePositionChart(self):
        self.positionFrame = Frame(width=370, height=100)
        self.table5 = PositionChartFrame(self.positionFrame, bd=1, relief=SUNKEN)
        self.table5.place(x=0, y=0)
        self.positionFrame.place(x=550, y=106)