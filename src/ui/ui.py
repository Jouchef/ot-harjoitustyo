from ui.konsoli_io import KonsoliIO
from repositories.storage_repository import StorageRepository
from database_connection import get_database_connection

COMMANDS = {
    "x": "x lopeta",
    "1": "1 lisää esine",
    "2": "2 hae esineet",

}

class UI:
    def __init__(self):
        self.io = KonsoliIO()
        self.storage_repository = StorageRepository(get_database_connection())

    def start(self):
        self.io.print("Tervetuloa esinevarastoon!")

        while True:
            self.print_menu()
            command = self.io.ask("komento: ")

            if not command in COMMANDS:
                self.io.printout("Virheellinen komento")
                self.print_menu()
                continue

            if command == "x":
                break
            elif command == "1":
                self.add_item()
            elif command == "2":
                self.get_items()

    def print_menu(self):
        self.io.print("Komennot:")
        for command, description in COMMANDS.items():
            self.io.print(f"{command} : {description}")
        self.io.print("Anna komento:")

    def add_item(self):
        name = self.io.ask("Anna esineen nimi:")
        amount  = self.io.ask("Anna esineiden määrä:")
        description = self.io.ask("Anna esineen kuvaus:")
        warehouse = self.io.ask("Anna varaston nimi:")
        self.storage_repository.add_to_warehouse(name, amount, description, warehouse)
        self.io.print(f"Lisätään esine {name} varastoon {warehouse}.")

    def get_items(self):
        self.io.print("Haetaan esineet...")
        for item in self.storage_repository.get_storage():
            self.io.print(item)
        
