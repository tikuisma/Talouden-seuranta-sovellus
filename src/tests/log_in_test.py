import unittest
from services.log_in import (new_user_creation, user_login)

class Testlog_in(unittest.TestCase):
	def setUp(self):
		print("Set up goes here")

	def test_new_user(self):
		user = "kissakoiramarsu"
		#answer = "Your account has been created. Next please log in."
		answer = "Check your usernames length requirements and try again."
		self.assertFalse(new_user_creation(user, answer)

	

