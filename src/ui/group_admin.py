from tkinter import Entry, Frame, Label, ttk, StringVar
from services.group_service import group_service, DuplicateGroupError, InvalidGroupError

class GroupAdmin:
    def __init__(self, root, handle_logout, ui):
        
        self._root = root
        self._handle_logout = handle_logout
        self._frame = None
        self._ui = ui

        self._group_name = None
        self._group_name_button = None
        self._table = None
        self._initialize()

    def _create_input_fields(self):
        self._group_name = StringVar()

        self._group_label = ttk.Label(self._frame, text="Luo tai poista ryhmä")
        self._group_label.grid(row=0, column=0, padx=10, pady=10)

        self._group_entry = ttk.Entry(self._frame, textvariable=self._group_name)
        self._group_entry.grid(row=0, column=1, padx=10, pady=10)

        self._group_create_button = ttk.Button(self._frame, text="Luo ryhmä", command=self._create_group)
        self._group_create_button.grid(row=0, column=2, padx=10, pady=10)

        self._group_delete_button = ttk.Button(self._frame, text="Poista ryhmä", command=self._delete_group)
        self._group_delete_button.grid(row=0, column=3, padx=10, pady=10)

    def _create_group(self):
        group_name = self._group_name.get()
        if len(group_name) == 0:
            self._ui.show_error("Ryhmän nimi ei voi olla tyhjä.")
            return
        try:
          group_service.create_group(group_name)
          self._update_group_table()
          self._ui.show_info(f"Ryhmä {group_name} luotu.")
        except DuplicateGroupError as e:
            print(f"Ryhmä {group_name} on jo olemassa")
            self._ui.show_error(e)

    def _delete_group(self):
        group_name = self._group_name.get()
        if group_name:
            try:
                group_service.delete_group(group_name)
                self._update_group_table()
                self._ui.show_info(f"Ryhmä {group_name} poistettu.")
            except InvalidGroupError as e:
                self._ui.show_error(e)
        else:
            self._ui.show_error("Poistettavan ryhmän nimi ei voi olla tyhjä.")

    def _create_group_table(self):
        self._table = ttk.Treeview(self._frame, columns=("name", "info"), show="headings")
        self._table.heading("name", text="Ryhmän nimi")
        self._table.heading("info", text="infoaa")
        self._table.bind('<Delete>', self._delete_groups)

        for group in self._get_list_of_groups():
            name = group.name

            data = (name, "info")
            self._table.insert("", "end", values=data)

        self._table.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    def _update_group_table(self):
        for row in self._table.get_children():
            self._table.delete(row)

        for group in self._get_list_of_groups():
            name = group.name

            data = (name, "info")
            self._table.insert("", "end", values=data)

    def _delete_groups(self, _):
        for i in self._table.selection():
            group_name = self._table.item(i)['values'][0]
            try:
                group_service.delete_group(group_name)
                self._ui.show_info(f"Ryhmä {group_name} poistettu.")
            except InvalidGroupError as e:
                self._ui.show_error(e)
        self._update_group_table()

    def _get_list_of_groups(self):
        return group_service.list_all_groups()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(self._root)
        self._table_frame = ttk.Frame(self._frame)

        self._create_input_fields()
        self._create_group_table()

        self._frame.pack(fill="both", padx=10, pady=10)



        