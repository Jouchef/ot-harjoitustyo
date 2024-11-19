import unittest
from services.user_service import UserService
from entities.user import User
from services.group_service import GroupService


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.group_service = GroupService()
        self.user_service = UserService(self.group_service)

    def test_user_can_be_added_to_users(self):
        self.user_service.add_user("user", "role", "group")
        self.assertEqual(self.user_service.list_users()[0], User("user", "role", "group"))

    def test_user_can_be_removed_from_users(self):
        self.user_service.add_user("test", "test", "test")
        # returns true if user can be removed.
        self.assertTrue(self.user_service.remove_user("test"))

    def test_list_users_returns_right_amount_of_users(self):
        self.user_service.add_user("test", "test", "test")
        self.user_service.add_user("test2", "test2", "test2")
        self.assertEqual(len(self.user_service.list_users()), 2)

    def test_listing_users_by_group_contains_right_amount(self):
        self.user_service.add_user("test", "test", "test")
        self.user_service.add_user("test2", "test2", "test")
        self.assertEqual(len(self.user_service.list_users_by_group("test")), 2)
        self.assertEqual(len(self.user_service.list_users_by_group("test2")), 0)