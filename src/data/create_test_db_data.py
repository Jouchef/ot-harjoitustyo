import sqlite3
from data.database_connection import get_database_connection


def fill_users_table(connection):
    try:
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO users (username, password) VALUES
            ('testi1', 'password1'),
            ('testi2', 'password2'),
            ('testi3', 'password3');
        ''')

        print("Testi käyttäjät lisätty users-tauluun")

        connection.commit()
    except sqlite3.DatabaseError as e:
        print(f"Tietokanta virhe: {e}")
        connection.rollback()


def fill_tables():
    connection = get_database_connection()
    try:
        fill_users_table(connection)
    except Exception as e:
        print(f"Virhe taulujen täyttämisessä: {e}")
    finally:
        connection.close()


if __name__ == "__main__":
    fill_tables()
