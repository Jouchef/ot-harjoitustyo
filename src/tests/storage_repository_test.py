import unittest
from repositories.storage_repository import StorageRepository


class TestStorageRepository(unittest.TestCase):
    def setUp(self):
        self.storage_repository.delete_all()
        self.name = "vasara"
        self.amount = 10
        self.description = "musta"
        self.warehouse = "varasto"

    def test_add_to_warehouse(self):
        self.storage_repository.add_to_warehouse(self.name, self.amount, self.description, self.warehouse)
        items = self.storage_repository.get_storage()
        self.assertEqual(len(items), 1)
        item = items[0]
        self.assertEqual(item.name, self.name)
        self.assertEqual(item.amount, self.amount)
        self.assertEqual(item.description, self.description)
        self.assertEqual(item.warehouse, self.warehouse)