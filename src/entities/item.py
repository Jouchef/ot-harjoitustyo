class Item:

    def __init__(self, name, amount, description, warehouse):
        self.name = name
        self.amount = amount
        self.description = description
        self.warehouse = warehouse

    def __str__(self):
        return (
            f"Item:\n"
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"Warehouse: {self.warehouse}\n"
        )

