import unittest
from datetime import datetime
from user_management import User, UserService, UserUtil

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(123456789, "John", "Doe", "john.doe@example.com", "Password123!", datetime(1990, 1, 1))

    def test_get_details(self):
        expected = "User ID: 123456789, Name: John Doe, Email: john.doe@example.com, Birthday: 1990-01-01"
        self.assertEqual(self.user.get_details(), expected)

    def test_get_age(self):
        self.assertGreaterEqual(self.user.get_age(), 33)

class TestUserService(unittest.TestCase):
    def setUp(self):
        UserService.users = {}
        self.user1 = User(123456789, "John", "Doe", "john.doe@example.com", "Password123!", datetime(1990, 1, 1))
        self.user2 = User(987654321, "Jane", "Smith", "jane.smith@example.com", "StrongPwd!", datetime(1995, 5, 10))
        UserService.add_user(self.user1)
        UserService.add_user(self.user2)

    def test_add_user(self):
        self.assertEqual(UserService.get_number(), 2)

    def test_find_user(self):
        found_user = UserService.find_user(123456789)
        self.assertEqual(found_user, self.user1)

    def test_delete_user(self):
        UserService.delete_user(123456789)
        self.assertEqual(UserService.get_number(), 1)

    def test_update_user(self):
        update_data = User(123456789, "Johnny", None, None, None, None)
        UserService.update_user(123456789, update_data)
        updated_user = UserService.find_user(123456789)
        self.assertEqual(updated_user.name, "Johnny")

    def test_get_number(self):
        self.assertEqual(UserService.get_number(), 2)

class TestUserUtil(unittest.TestCase):
    def test_generate_user_id(self):
        user_id = UserUtil.generate_user_id()
        self.assertTrue(isinstance(user_id, int))
        self.assertEqual(len(str(user_id)), 9)

    def test_generate_password(self):
        password = UserUtil.generate_password()
        self.assertTrue(UserUtil.is_strong_password(password))

    def test_is_strong_password(self):
        self.assertTrue(UserUtil.is_strong_password("StrongPwd!"))
        self.assertFalse(UserUtil.is_strong_password("weak"))

    def test_generate_email(self):
        email = UserUtil.generate_email("John", "Doe", "example.com")
        self.assertEqual(email, "john.doe@example.com")

    def test_validate_email(self):
        self.assertTrue(UserUtil.validate_email("john.doe@example.com"))
        self.assertFalse(UserUtil.validate_email("invalidemail"))

if __name__ == '__main__':
    unittest.main()