from tkinter import Entry, Frame, Label, ttk, StringVar
from services.user_service import user_service, InvalidCredentialsError, DuplicateUserError


class LoginRegister(Frame):
    """Käyttäjän kirjautumis- ja rekisteröitymisnäkymä."""

    def __init__(self, root, handle_login, handle_register, ui):
        #Tarvitaan "super" koska yhdellä sivulla on kaksi eri näkymää
        super().__init__(root)
        self._ui = ui
      
        self._handle_login = handle_login
        self._handle_register = handle_register

        self._create_login_view()
        self._create_register_view()

        self.pack(fill="both", expand=True)

    def _on_login(self):
        username = self.username_login.get()
        password = self.password_login.get()

        if not username or not password:
            self._ui.show_error("Täytä molemmat kentät!")
        else:
            self._ui.clear_error()
            print(f"Kirjautumisyritys: {username}, {password}")
            try:
                user_service.login(username, password)
                print("Kirjautuminen onnistui!")
                self._handle_login()
            except InvalidCredentialsError as e:
                self._ui.show_error(str(e))
            

    def _on_register(self):
        username = self.username_register.get()
        password = self.password_register.get()

        if not username or not password:
            self._ui.show_error("Täytä molemmat kentät!")
        else:
            self._ui.clear_error()
            print(f"Rekisteröitymisyritys: {username}, {password}")
            try:
                
                user_service.register(username, password)
                print("Rekisteröityminen onnistui!")
                self._ui.show_error("Rekisteröityminen onnistui")
                self._handle_register()
            except DuplicateUserError as e:
                self._ui.show_error(f"virhe: {e}")


    def _create_login_view(self):
        login_frame = Frame(self, bg="black", padx=20, pady=20)
        login_frame.place(relx=0.25, rely=0.5, anchor="center")

        # Otsikko
        Label(login_frame, text="Kirjaudu", fg="white", bg="black", font=("Arial", 20)).grid(
            row=0, column=0, columnspan=2, pady=10
        )

        # Käyttäjätunnus
        Label(login_frame, text="Käyttäjätunnus:", fg="white", bg="black").grid(row=1, column=0, sticky="w")
        self.username_login = StringVar()
        ttk.Entry(login_frame, textvariable=self.username_login).grid(row=1, column=1, pady=5)

        # Salasana
        Label(login_frame, text="Salasana:", fg="white", bg="black").grid(row=2, column=0, sticky="w")
        self.password_login = StringVar()
        ttk.Entry(login_frame, textvariable=self.password_login, show="*").grid(row=2, column=1, pady=5)

        # Kirjaudu-painike
        login_button = ttk.Button(
            login_frame, 
            text="Kirjaudu", 
            command=self._on_login
        )
        login_button.grid(row=3, column=0, columnspan=2, pady=10)


    def _create_register_view(self):
        """Luo rekisteröitymisnäkymän oikealle."""
        register_frame = Frame(self, bg="black", padx=20, pady=20)
        register_frame.place(relx=0.75, rely=0.5, anchor="center")

        # Otsikko
        Label(register_frame, text="Rekisteröidy", fg="white", bg="black", font=("Arial", 20)).grid(
            row=0, column=0, columnspan=2, pady=10
        )

        # Käyttäjätunnus
        Label(register_frame, text="Käyttäjätunnus:", fg="white", bg="black").grid(row=1, column=0, sticky="w")
        self.username_register = StringVar()
        Entry(register_frame, textvariable=self.username_register).grid(row=1, column=1, pady=5)

        # Salasanakenttä
        Label(register_frame, text="Salasana:", fg="white", bg="black").grid(row=2, column=0, sticky="w")
        self.password_register = StringVar()
        Entry(register_frame, textvariable=self.password_register, show="*").grid(row=2, column=1, pady=5)

        # Rekisteröidy-painike
        ttk.Button(register_frame, text="Rekisteröidy", command=self._on_register).grid(
            row=3, column=0, columnspan=2, pady=10
        )
