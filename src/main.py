from ui.ui import UI
from initialize_database import initialize_database

def main():
    import sys; print(sys.path)
    initialize_database()
    UI().start()




if __name__ == "__main__":
    main()