from tkinter import Frame
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Utilities.DbUtility import getDataForEmployeePosition


class PositionChartFrame(Frame):
    def __init__(self, root, **kwargs):
        Frame.__init__(self)
        list = getDataForEmployeePosition()
        labels = list[0]
        sizes = list[1]
        pcts = [f'{s} {l}\n({s * 100 / sum(sizes):.2f}%)' for s, l in zip(sizes, labels)]

        fig = matplotlib.figure.Figure(figsize=(4, 1))
        ax = fig.add_subplot(111)
        ax.pie(sizes,
               startangle=90,
               labels=pcts,)

        label = ax.annotate("Pozicionet", xy=(0, 0), fontsize=8, ha="center")
        circle = matplotlib.patches.Circle((0, 0), 0.7, color='white')
        ax.add_artist(circle)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()
        canvas.draw()

