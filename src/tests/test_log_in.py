import unittest
from services.log_in import (new_user_creation, user_login)

class TestLogIn(unittest.TestCase):
    def setUp(self):
        pass

    def test_new_user(self):
        user = "kissakoiramarsu"
        answer = "Check your usernames length requirements and try again."
        self.assertEqual(new_user_creation(user), answer)
        user2 = "tero"
        answer2 = "Username is already taken. Try another one."
        self.assertEqual(new_user_creation(user2), answer2)

    def test_users_existing(self):
        ans = "User not found. Please check spelling or create new user."
        user = "timotei"
        self.assertEqual(user_login(user), ans)
        ans2 = "Signing in"
        user2 = "tero"
        self.assertEqual(user_login(user2), ans2)
