import tkinter as tk

from tksheet import Sheet


class EmployeeSalaryTable(tk.Frame):
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
                                         "copy",))



        # __________ CHANGING THEME __________

        # self.sheet_demo.change_theme("dark")

        # __________ HIGHLIGHT / DEHIGHLIGHT CELLS __________

        self.sheet_demo.highlight_cells(column=0, bg="#3A3A3A", fg="white" , canvas= 'header')
        self.sheet_demo.highlight_cells(column=1, bg="#3A3A3A", fg="white", canvas=
        'header')
        self.sheet_demo.highlight_cells(column=2, bg="#3A3A3A", fg="white", canvas= 'header')
        self.sheet_demo.highlight_cells(column=3, bg="#3A3A3A", fg="white" , canvas= 'header')
        self.sheet_demo.highlight_cells(column=4, bg="#3A3A3A", fg="white", canvas="header")
        self.sheet_demo.highlight_cells(column=5, bg="#3A3A3A", fg="white", canvas="header")

        self.records = []

        # self.sheet_demo.column_width(column=0, width=100)
        self.sheet_demo.set_column_widths([180 for c in range(4)])
        # Madhesia e headerit sipas kolones
        # self.sheet_demo.column_width(column=2, width=100)
        # self.sheet_demo.column_width(column=3, width=125)


        # __________ SETTING HEADERS __________

        self.headers = [f" {c}" for c in ( 'Emri', 'Mbiemri', 'Data', 'Oret')]

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
        self.records = recordData
        self.data = [[f" {c}" for c in r] for r in  self.records]
        self.sheet_demo.data_reference(self.data)
        self.sheet_demo.set_column_widths([180 for c in range(4)])
        self.sheet_demo.refresh(True, True)

    def getData(self):
        return self.records
