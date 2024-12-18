from datetime import datetime

class CalendarReposetory:
    def __init__(self, connection):
        self.connection = connection

    def ensure_positive_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

    def add_for_user(self, username, amount):
        """Adds calendars to user. Amount must be positive."""
        self.ensure_positive_amount(amount)
        try:
            cursor = self.connection.cursor()
            current_date = datetime.now()
            cursor.execute(
                "INSERT INTO user_calendars (username, amount, date) VALUES (?, ?, ?)", 
                (username, amount, current_date))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def add_for_group(self, group_name, amount):
        """Adds calendars to group. Amount must be positive."""
        self.ensure_positive_amount(amount)
        try:
            cursor = self.connection.cursor()
            current_date = datetime.now()
            cursor.execute(
                "INSERT INTO group_calendars (group_name, amount, date) VALUES (?, ?, ?)", 
                (group_name, amount, current_date))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def take_from_user(self, username, amount):
        """Takes calendars from user. Amount must be positive."""
        self.ensure_positive_amount(amount)
        try:
            cursor = self.connection.cursor()
            current_date = datetime.now()
            amount = -amount
            cursor.execute(
                "INSERT INTO user_calendars (username, amount, date) VALUES (?, ?, ?)", 
                (username, amount, current_date))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def take_from_group(self, group_name, amount):
        """Takes calendars from group. Amount must be positive."""
        self.ensure_positive_amount(amount)
        try:
            cursor = self.connection.cursor()
            current_date = datetime.now()
            amount = -amount
            cursor.execute(
                "INSERT INTO group_calendars (group_name, amount, date) VALUES (?, ?, ?)", 
                (group_name, amount, current_date))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def get_user_calendar_events(self, username):
        """Returns all calendar events for a user."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM user_calendars WHERE username = ?", 
                           (username,))
            rows = cursor.fetchall()
            return [row for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()

    def get_group_calendar_events(self, group_name):
        """Returns all calendar events in a group."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM group_calendars WHERE group_name = ?", 
                           (group_name,))
            rows = cursor.fetchall()
            return [row for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()

    def get_users_calendar_amount(self, username):
        """Returns sum of calendars for a given user."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT SUM(amount)"
                           "FROM user_calendars" 
                           "WHERE username = ?", 
                           (username,))
            row = cursor.fetchone()
            return row[0] if row else 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
        finally:
            cursor.close()

    def get_groups_calendar_amount(self, group_name):
        """Returns sum of calendars in a given group. Not the ones that belong to users."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT SUM(amount)" 
                "FROM group_calendars" 
                "WHERE group_name = ?", 
                (group_name,))
            row = cursor.fetchone()
            return row[0] if row else 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0
        finally:
            cursor.close()

    def get_groups_users_calendar_events(self, group_name):
        """Returns all users' calendar events in a group."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT uc.* FROM user_calendars uc "
                "JOIN group_participants gp ON uc.username = gp.username "
                "WHERE gp.group_name = ?", 
                (group_name,)
            )
            rows = cursor.fetchall()
            return [row for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()
