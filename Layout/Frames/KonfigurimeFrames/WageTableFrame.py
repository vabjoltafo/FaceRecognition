import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Label, Combobox

import PIL
from tksheet import Sheet

from Repositories.EmployeeRepository import getAllEmployeeNameAndSurname
from Repositories.WageEmployeeRepository import selectDataToDisplay, selectWageByEmployeeId, deleteWage, updateWage
from Utilities.Convertors import getEmployeeFullNameList
from Utilities.DbUtility import insertCrudOperations, isANumber


class WageTableFrame(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.sheet_demo = Sheet(root,
                                width=2500,
                                height=430,
                                align="center",
                                header_align="center",
                                row_index_align="center",
                                row_index_width= 50,
                                total_rows=1000,
                                total_columns=4)
        self.sheet_demo.enable_bindings(("single_select",  # "single_select" or "toggle_select"
                                         "drag_select",  # enables shift click selection as well
                                         "column_drag_and_drop",
                                         "row_drag_and_drop",
                                         "row_select",
                                         "column_width_resize",
                                         "double_click_column_resize",
                                         # "row_width_resize",
                                         # "column_height_resize",
                                         "arrowkeys",
                                         "row_height_resize",
                                         "double_click_row_resize",
                                         "right_click_popup_menu",
                                         "rc_select",
                                         "rc_delete_row",
                                         "copy",
                                         "undo",))



        # __________ CHANGING THEME __________

        # self.sheet_demo.change_theme("dark")

        # __________ HIGHLIGHT / DEHIGHLIGHT CELLS __________




        self.records = []

        self.response = ()
        self.records = insertCrudOperations(selectDataToDisplay())

        # if name is "Filtro sipas emrit" or name is ' ':
        #     # self.dateFormat = getTheDateFromDictionary(self.date)
        #     self.records = getTheInfomationFromEmployees()
        # else:
        #     self.records = getEmployeesByName(name)

        # Vendosja e te dhenave

        self.data = [[f" {c}" for c in r] for r in self.records]
        self.sheet_demo.data_reference(self.data)

        # self.sheet_demo.column_width(column=0, width=100)
        self.sheet_demo.set_column_widths([120 for c in range(6)])
        # Madhesia e headerit sipas kolones
        # self.sheet_demo.column_width(column=2, width=100)
        # self.sheet_demo.column_width(column=3, width=125)

        for i in range(len(self.data)):
            self.sheet_demo.highlight_cells(row=i, column=4, bg="white", fg="orange", canvas="table")
            self.sheet_demo.highlight_cells(row= i, column=5, bg="white", fg="red", canvas="table")

        self.sheet_demo.highlight_cells(column=0, bg="#3A3A3A", fg="white", canvas='header')
        self.sheet_demo.highlight_cells(column=1, bg="#3A3A3A", fg="white", canvas='header')
        self.sheet_demo.highlight_cells(column=2, bg="#3A3A3A", fg="white", canvas='header')
        self.sheet_demo.highlight_cells(column=3, bg="#3A3A3A", fg="white", canvas='header')
        self.sheet_demo.highlight_cells(column=4, bg="#3A3A3A", fg="white", canvas='header')
        self.sheet_demo.highlight_cells(column=5, bg="#3A3A3A", fg="white", canvas='header')


        # __________ SETTING HEADERS __________

        self.headers = [f" {c}" for c in ('Emri', 'Mbiemri', 'Pozicioni', 'Paga Orare', 'Ndrysho', 'Elemino')]

        self.sheet_demo.headers(self.headers)


        self.sheet_demo.extra_bindings([
            ("cell_select", self.cell_select),
            ("shift_cell_select", self.shift_select_cells),
            ("drag_select_cells", self.drag_select_cells),
            ("ctrl_a", self.ctrl_a),
            ("row_select", self.row_select),
            ("shift_row_select", self.shift_select_rows),
            ("drag_select_rows", self.drag_select_rows),
            ("column_select", self.column_select),
            ("shift_column_select", self.shift_select_columns),
            ("drag_select_columns", self.drag_select_columns),
        ]
        )

        self.sheet_demo.place(x=0, y=160)

    def cell_select(self, response):
        self.response = response
        if self.response[2] is 5:
           self.deleteWage()
        elif self.response[2] is 4:
            self.openEditForm()
        print(response)

    def shift_select_cells(self, response):
        print(response)

    def drag_select_cells(self, response):
        pass
        # print (response)

    def ctrl_a(self, response):
        print(response)

    def row_select(self, response):
        self.response = response
        test = self.sheet_demo.get_row_data(self, response)
        print(response, test)

    def shift_select_rows(self, response):
        print(response)

    def drag_select_rows(self, response):
        pass
        # print (response)

    def column_select(self, response):
        print(response)

    def shift_select_columns(self, response):
        print(response)

    def drag_select_columns(self, response):
        pass
        # print (response)

    def getResponse(self):
        return self.response

    def updateTable(self, recordData):
        self.records = insertCrudOperations(recordData)
        self.data = [[f" {c}" for c in r] for r in self.records]
        self.sheet_demo.data_reference(self.data)
        self.sheet_demo.set_column_widths([120 for c in range(6)])
        self.sheet_demo.refresh(True, True)

    def getData(self):
        return self.records

    def deleteWage(self):
        if self.getResponse() is ():
            messagebox.showerror('Kujdes!', 'Zgjidhni një punonjes në tabelë!')
        else:
            index = int(self.response[1])
            tuple = self.getData()
            wageId = selectWageByEmployeeId(tuple[index][0] + " " + tuple[index][1])[0]
            # print(wageId)
            MsgBox = messagebox.askquestion('Fshirje', 'Jeni i sigurt që doni të fshini punonjesin '
                                            + tuple[index][0] + ' ' + tuple[index][1] + '?',
                                            icon='warning')
            if MsgBox == 'yes':
                deleteWage(wageId)
                # messagebox.showinfo('Info', 'Përdoruesi u fshi me sukses!')
                data = insertCrudOperations(selectDataToDisplay())
                self.updateTable(data)

    def openEditForm(self):
        if self.getResponse() is ():
            messagebox.showerror('Kujdes!', 'Zgjidhni një punonjes në tabelë!')
        else:
            self.var1 = tk.IntVar()
            index = int(self.getResponse()[1])
            tuple = self.getData()
            wage = selectWageByEmployeeId(tuple[index][0] + " " + tuple[index][1])
            self.data = wage
            self.width = 400
            self.height = 220
            self.toplevel_dialog = tk.Toplevel(self)
            self.toplevel_dialog.minsize(self.width, self.height)
            self.screen_width = self.toplevel_dialog.winfo_screenwidth()
            self.screen_height = self.toplevel_dialog.winfo_screenheight()
            self.x = (self.screen_width / 2) - (self.width / 2)
            self.y = (self.screen_height / 2) - (self.height / 2)
            self.toplevel_dialog.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
            self.toplevel_dialog.transient(self)
            self.toplevel_dialog.protocol("WM_DELETE_WINDOW", self.Close_Toplevel)

            self.toplevel_dialog_label = Label(self.toplevel_dialog, text='Ndrysho',
                                               font=("Sans-Serif", 15, 'bold')).pack()
            self.FULL_NAME1 = tk.StringVar()
            self.WAGE1 = tk.StringVar()

            self.FULL_NAME1.set(tuple[index][0] + " " + tuple[index][1])
            self.WAGE1.set(float(wage[2]))

            listOfEmployees = getEmployeeFullNameList(getAllEmployeeNameAndSurname())
            self.punonjesiLabel = Label(self.toplevel_dialog, text='Punonjësi', font=('Sans-Serif', 13, 'bold')).place(
                x=20, y=50)
            self.punonjesiEntry1 = Combobox(self.toplevel_dialog, width=16, value=listOfEmployees,
                                            textvariable=self.FULL_NAME1, state='disabled',
                                            font=('Sans-Serif', 13)).place(x=170, y=50)

            self.pagaorareLabel = Label(self.toplevel_dialog, text='Paga orare', font=('Sans-Serif', 13, 'bold')).place(
                x=20, y=90)
            self.pagaorareEntry1 = tk.Entry(self.toplevel_dialog, width=27, textvariable=self.WAGE1).place(x=170, y=90,
                                                                                                           height=25)
            self.orare = tk.Checkbutton(self.toplevel_dialog, text='Orar',variable=self.var1, onvalue=1, offvalue=0)
            self.orare.place(x=190, y=120)

            RuajImage = PIL.Image.open("Layout\\images\\RuajButton.png")
            RuajImage = RuajImage.resize((450, 300), PIL.Image.ANTIALIAS)
            self.RuajImage = PIL.ImageTk.PhotoImage(RuajImage)
            self.toplevel_dialog_yes_button = tk.Button(self.toplevel_dialog, image=self.RuajImage, bd=0, width=55,
                                                        height=45, command=self.updateWage)

            self.toplevel_dialog_yes_button.place(x=140, y=180)

            AnuloImage = PIL.Image.open("Layout\\images\\AnuloButton.png")
            AnuloImage = AnuloImage.resize((400, 300), PIL.Image.ANTIALIAS)
            self.AnuloImage = PIL.ImageTk.PhotoImage(AnuloImage)

            self.toplevel_dialog_no_button = tk.Button(self.toplevel_dialog, bd=0, height=45, width=55,
                                                       image=self.AnuloImage, command=self.Close_Toplevel)

            self.toplevel_dialog_no_button.place(x=200, y=180)

    def updateWage(self):
        if len(self.WAGE1.get()) is 0:
            messagebox.showerror("Kujdes", "Paga s'mund te jete bosh!")
        else:
            if isANumber(self.WAGE1.get()):
                self.getCheckBoxValue()
                updateWage(self.data[0], self.WAGE1.get(), self.getCheckBoxValue())
                data = insertCrudOperations(selectDataToDisplay())
                # self.table = WageTableFrame(self)
                # self.table.place(x=200, y=140)
                self.updateTable(data)
                self.Close_Toplevel()
            else:
                messagebox.showerror("Kujdes", "Paga duhet te jete nje numer!")

    def Close_Toplevel(self):
        self.toplevel_dialog.destroy()

    def getCheckBoxValue(self):
        return str(self.var1.get())