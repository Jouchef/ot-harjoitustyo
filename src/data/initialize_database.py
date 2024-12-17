from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    #Mahdollistaa taulujen poiston missä vaan järjestyksessä
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

    #Viittaukset takaisin päälle
    cursor.execute('''
                   PRAGMA foreign_keys = ON;
                   ''')

    connection.commit()



def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
        
        create table user_calendars (
            id integer primary key autoincrement,
            username text,
            amount integer,
            date text,
            foreign key (username) references users(username)
        );
                   
        create table user_money (
            id integer primary key autoincrement,
            username text,
            amount integer,
            date text,
            foreign key (username) references users(username)
          );
                   
        create table groups (
            name text primary key
        );
                   
        create table group_leaders (
            group_name text,
            username text,
            primary key (group_name, username),
            foreign key (group_name) references groups(name),
            foreign key (username) references users(username)
        );
        
        create table group_participants (
            group_name text,
            username text,
            primary key (group_name, username),
            foreign key (group_name) references groups(name),
            foreign key (username) references users(username)
        );
        
        create table group_calendars (
            id integer primary key autoincrement,
            group_name text,
            amount integer,
            date text,
            foreign key (group_name) references groups(name)
        );
        
            
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
    