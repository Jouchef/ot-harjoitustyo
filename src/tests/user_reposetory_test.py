import unittest
from reposetory.user_reposetory import UserReposetory
from data.database_connection import get_database_connection
from data.initialize_database import initialize_database

class TestUserReposetory(unittest.TestCase):
    def setUp(self):
        self.connection = get_database_connection()
        self.user_reposetory = UserReposetory(self.connection)
        self.user_reposetory.add_user("Jonne", "es")

    def tearDown(self):
        initialize_database()
        

    def test_fetch_users(self):
        users = self.user_reposetory.fetch_users()
        self.assertEqual(len(users), 1)

    def test_fetch_users_returns_users(self):
        users = self.user_reposetory.fetch_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "Jonne")
        self.assertEqual(users[0].password, "es")

    def test_adding_user_succesfully_returns_true(self):
        result = self.user_reposetory.add_user("Janne", "ed")
        self.assertTrue(result)

    def test_adding_user_with_existing_username_returns_false(self):
        result = self.user_reposetory.add_user("Jonne", "es")
        self.assertFalse(result)

    def test_remove_user_succesfully_returns_true(self):
        result = self.user_reposetory.remove_user("Jonne")
        self.assertTrue(result)

    def test_remove_user_with_non_existing_username_returns_false(self):
        result = self.user_reposetory.remove_user("niilo napakka")
        self.assertFalse(result)

    def test_get_user_returns_user(self):
        user = self.user_reposetory.get_user("Jonne")
        self.assertEqual(user.username, "Jonne")

    def test_get_non_existent_user_returns_none(self):
        user = self.user_reposetory.get_user("niilo napakka")
        self.assertEqual(user, None)