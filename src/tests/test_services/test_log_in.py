import unittest
from services.log_in import (new_user_creation, user_login)
from database_services.user_database import UserDatabase

class TestLogIn(unittest.TestCase):
    def setUp(self):
        self.userdatabase = UserDatabase()
        self.userdatabase.dcursor.execute('''DELETE FROM Users''')
        new_user_creation("hertta", self.userdatabase)

    def test_new_user(self):
        user = "kissakoiramarsu"
        answer = "Check your usernames length requirements and try again."
        self.assertEqual(new_user_creation(user, self.userdatabase), answer)
        user3 = "kerttu"
        answer3 = "Your account has been created. Next please log in."
        self.assertEqual(new_user_creation(user3, self.userdatabase), answer3)
        user2 = "kerttu"
        answer2 = "Username is already taken. Try another one."
        self.assertEqual(new_user_creation(user2, self.userdatabase), answer2)

    def test_users_existing(self):
        ans = "User not found. Please check spelling or create new user."
        user = "timotei"
        self.assertEqual(user_login(user, self.userdatabase), ans)
        ans2 = "Signing in"
        user2 = "hertta"
        self.assertEqual(user_login(user2, self.userdatabase), ans2)
