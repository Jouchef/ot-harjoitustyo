from entities.group import Group
from data.database_connection import get_database_connection



class GroupReposetory:
    def __init__(self, connection):
        self.connection = connection

    def create_group(self, name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO groups (name) VALUES (?)", (name,))
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            print(f"Ryhmän luomisessa tapahtui virhe: {e}")
            return False
        finally:
            cursor.close()

    def get_group(self, group_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM groups WHERE name = ?", (group_name,))
            row = cursor.fetchone()
            if row:
                return Group(row['name'])
            return None
        except Exception as e:
            print(f"Ryhmän hakemisessa tapahtui virhe: {e}")
            return None
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
            print(f"Ryhmän poistamisessa tapahtui virhe: {e}")
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
            print(f"Ryhmien listaamisessa tapahtui virhe: {e}")
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
            print(f"Henkilön lisäämisessä ryhmään tapahtui virhe: {e}")
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
            print(f"Henkilön poistamisessa ryhmästä tapahtui virhe: {e}")
            return False
        finally:
            cursor.close()


group_reposetory = GroupReposetory(get_database_connection())
