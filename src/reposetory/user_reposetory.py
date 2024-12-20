from entities.user import User
from data.database_connection import get_database_connection


class UserReposetory:
    def __init__(self, connection):
        self.connection = connection

    def fetch_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            return [User(user['username'], user['password']) for user in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()

    def add_user(self, username, password):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def remove_user(self, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE username = ?",
                           (username,))
            if cursor.rowcount == 0:
                return False
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def get_user(self, username):
        """Hakee käyttäjän käyttäjätunnuksen perusteella.
        
        Args:
            username: Merkkijono, käyttäjätunnus

        Returns:
            User: Käyttäjä-olio, jos käyttäjä löytyy, muuten None
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            return User(user['username'], user['password']) if user else None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            cursor.close()

    def get_users_groups(self, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT group_name FROM group_participants WHERE username = ?", (username,))
            rows = cursor.fetchall()
            return [row['group_name'] for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()

    def get_users_money_events(self, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM user_money WHERE username = ?", (username,))
            rows = cursor.fetchall()
            return [row for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()

    def get_users_money_balance(self, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT SUM(amount) FROM user_money WHERE username = ?", (username,))
            row = cursor.fetchone()
            return row[0] if row else 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
        finally:
            cursor.close()

user_reposetory = UserReposetory(get_database_connection())
