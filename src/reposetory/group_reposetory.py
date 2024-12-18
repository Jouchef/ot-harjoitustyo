from entities.group import Group


class GroupReposetory:
    def __init__(self, connection):
        self.connection = connection

    def create_group(self, name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO groups (name) VALUES (?)", (name))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def delete_group(self, group_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM groups WHERE name = ?", (group_name,))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def list_all_groups(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM groups")
            rows = cursor.fetchall()
            return [Group(row['name']) for row in rows]
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            cursor.close()

    def add_participant_to_group(self, group_name, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO group_participants (group_name, username) VALUES (?, ?)", 
                (group_name, username)
            )
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()

    def remove_participant_from_group(self, group_name, username):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "DELETE FROM group_participants WHERE group_name = ? AND username = ?", 
                (group_name, username)
            )
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            cursor.close()
