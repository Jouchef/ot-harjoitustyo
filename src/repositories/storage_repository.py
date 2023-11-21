from entities.item import Item
from database_connection import get_database_connection

class StorageRepository:
    def __init__(self, connection):
        self.connection = connection

    def add_to_warehouse(self, name, amount, description, warehouse):

        cursor = self.connection.cursor()

        cursor.execute("insert into items (name, amount, description, warehouse) values (?, ?, ?, ?)",
                       [name, amount, description, warehouse])
        
        self.connection.commit()

        print("Tulostetaan varaston sisältö:")
        for item in self.get_storage():
            print(item)



    def get_storage(self):
            
            cursor = self.connection.cursor()
    
            cursor.execute("select * from items")
    
            result = []
            for row in cursor:
                result.append(Item(row[0], row[1], row[2], row[3]))
    
            return result

    
    def delete_all(self):
        cursor = self.connection.cursor()

        cursor.execute("delete from items")

        self.connection.commit()