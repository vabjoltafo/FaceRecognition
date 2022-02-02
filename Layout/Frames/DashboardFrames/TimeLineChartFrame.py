from tkinter import Frame
import matplotlib
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas.plotting import register_matplotlib_converters
from Utilities.DbUtility import getInformation
register_matplotlib_converters()

class TimeLineChartFrame(Frame):
    def __init__(self, root, **kwargs):
        Frame.__init__(self)

        full_list = getInformation()

        fig = matplotlib.figure.Figure(figsize=(8, 2))
        ax = fig.add_subplot(111)
        t = matplotlib.dates.DateFormatter('%d')
        ax.xaxis.set_major_formatter(t)

        ax.grid(True, color="#93a1a1", alpha=0.3)
        ax.plot(full_list[0], full_list[1], color="#CF1613")
        ax.set_xticks(full_list[0])
        ax.set_yticks(full_list[1])
        ax.set_title("Nr. i punonjesve te pranishem ne 14 ditet e fundit")
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()
        canvas.draw()

