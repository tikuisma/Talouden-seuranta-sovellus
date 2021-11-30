import unittest
from services.log_in import new_user_creation, user_login

class TestLog_in(unittest.TestCase):
	def setUp(self):
		print("Set up goes here")
	
	def test_new_user(self):
		user = "kissa"
		answer = "Your account has been created. Next please log in."
		self.assertEqual(new_user_creation(user), answer)
		self.assertEqual(user_login(user), "Signing in")
