from data.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    # Mahdollistaa taulujen poiston missä vaan järjestyksessä
    cursor.execute('''
                   PRAGMA foreign_keys = OFF;
                   ''')

    tables = [
        "group_calendars",
        "group_participants",
        "group_leaders",
        "groups",
        "user_money",
        "user_calendars",
        "users"
    ]

    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table};")

    # Viittaukset takaisin päälle
    cursor.execute('''
                   PRAGMA foreign_keys = ON;
                   ''')

    print("Taulut poistettu")

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            username TEXT PRIMARY KEY,
            password TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE user_calendars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            amount INTEGER,
            date TEXT,
            FOREIGN KEY (username) REFERENCES users(username)
        );
    ''')

    cursor.execute('''
        CREATE TABLE user_money (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            amount INTEGER,
            date TEXT,
            FOREIGN KEY (username) REFERENCES users(username)
        );
    ''')

    cursor.execute('''
        CREATE TABLE groups (
            name TEXT PRIMARY KEY
        );
    ''')

    cursor.execute('''
        CREATE TABLE group_leaders (
            group_name TEXT,
            username TEXT,
            PRIMARY KEY (group_name, username),
            FOREIGN KEY (group_name) REFERENCES groups(name),
            FOREIGN KEY (username) REFERENCES users(username)
        );
    ''')

    cursor.execute('''
        CREATE TABLE group_participants (
            group_name TEXT,
            username TEXT,
            PRIMARY KEY (group_name, username),
            FOREIGN KEY (group_name) REFERENCES groups(name),
            FOREIGN KEY (username) REFERENCES users(username)
        );
    ''')

    cursor.execute('''
        CREATE TABLE group_calendars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT,
            amount INTEGER,
            date TEXT,
            FOREIGN KEY (group_name) REFERENCES groups(name)
        );
    ''')

    print("Taulut luotu")

    connection.commit()


def fill_users_table(connection):
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO users (username, password) VALUES
        ('testi1', 'password1'),
        ('testi2', 'password2'),
        ('testi3', 'password3');
    ''')

    print("Testi käyttäjät lisätty users-tauluun")

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
