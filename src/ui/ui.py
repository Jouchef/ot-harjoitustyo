from tkinter import Menu, Frame
from tkinter.ttk import Label, Button, Style
from ui.login_register import LoginRegister
from ui.group_admin import GroupAdmin

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._menu = None

        self._create_error_frame()

    def start(self):
        """Käynnistää käyttöliittymän."""
        #self._show_login_register_view()
        self._show_group_admin_view()

    def _create_error_frame(self):
        """Luo virheilmoituksille tarkoitetun kehyksen."""
        self.error_frame = Frame(self._root)

        self.style = Style()
        self.style.configure("Error.TLabel", foreground="red")

        self.error_label = Label(self.error_frame, text="", style="Error.TLabel", anchor="center")
        self.error_label.pack(side="left", fill="x", expand=True, padx=10, pady=5)

        # "X"-nappi virheilmoituksen sulkemiseen
        self.error_close_button = Button(self.error_frame, text="X", command=self.clear_error)
        self.error_close_button.pack(side="left", padx=5)

    def _show_menubar_for_logged_in(self):
        print("show menubar_for_logged_in")
        self._init_menubar()
        self._menu.add_command(label="Kirjaudu ulos", command=self._show_login_register_view)
        self._menu.add_command(label="testi", command=self._show_login_register_view)

    def _show_menubar_for_login(self):
        """Näyttää menupalkin (esim. kirjautumisen jälkeen)."""
        print("show menubar_for_login")
        self._init_menubar()
        self._menu.add_command(label="Kirjaudu ulos", command=self._show_login_register_view)

    def _init_menubar(self):
        """Alustaa menupalkin"""
        self._menu = Menu(self._root)
        self._root.config(menu=self._menu)
        self._menu.delete(0, "end")

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän ja menupalkin."""
        if self._current_view:
            self._current_view.destroy()

        self.clear_error()
        self._current_view = None

    def _show_login_register_view(self):
        """Näyttää kirjautumis- ja rekisteröitymisnäkymän."""
        self._hide_current_view()
        self._current_view = LoginRegister(
            self._root,
            self._show_group_admin_view,
            self._show_login_register_view,
            self
        )
        self._show_menubar_for_login()

    def _show_group_admin_view(self):
        """Näyttää ryhmänhallintanäkymän."""
        self._hide_current_view()
        self._current_view = GroupAdmin(
            self._root, 
            self._show_login_register_view,
            self
        )
        self._show_menubar_for_logged_in()

    def show_error(self, message):
        """Näyttää punaisen virheilmoituksen alareunassa."""
        self.error_label.config(text=message)
        self.style.configure("Error.TLabel", foreground="red")
        self.error_frame.pack(side="bottom", fill="x", pady=5)

    def show_info(self, message):
        """Näyttää vihreän tiedotteen alareunassa."""
        self.error_label.config(text=message)
        self.style.configure("Error.TLabel", foreground="green")
        self.error_frame.pack(side="bottom", fill="x", pady=5)

    def clear_error(self):
        """Tyhjentää virheilmoituksen."""
        self.error_label.config(text="")
        self.error_frame.pack_forget()
