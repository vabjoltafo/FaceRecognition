from tkinter import Frame

import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Repositories.EmployeeRepository import getMaleEmployees, getFemaleEmployees


class GenderChartFrame(Frame):
    def __init__(self, root, **kwargs):
        Frame.__init__(self)
        self.width = 200
        self.height = 200

        labels = 'Meshkuj', 'Femra'
        sizes = getMaleEmployees(), getFemaleEmployees()
        pcts = [f'{s} {l}\n({s * 100 / sum(sizes):.2f}%)' for s, l in zip(sizes, labels)]

        fig = matplotlib.figure.Figure(figsize=(4, 1))
        ax = fig.add_subplot(111)
        ax.pie(sizes,
               startangle=90,
               labels=pcts,
               colors=["tab:green", "tab:orange"])

        label = ax.annotate("Gjinia", xy=(0, 0), fontsize=10, ha="center")
        circle = matplotlib.patches.Circle((0, 0), 0.7, color='white')
        ax.add_artist(circle)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.get_tk_widget().pack()
        canvas.draw()

