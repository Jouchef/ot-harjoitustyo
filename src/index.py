from tkinter import Tk

from ui.ui import UI



def main():
    print("mainissa")
    window = Tk()
    window.title("Adventtikalenteriwelho")

    window.geometry("1000x800")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()