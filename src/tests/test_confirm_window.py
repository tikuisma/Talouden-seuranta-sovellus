import unittest
from database_services.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.database.dcursor.execute('''DELETE FROM Database''')
        self.database.writing_database("marsu", "expense", "Pets", "July", 2021, 12)
        self.database.writing_database("marsu", "expense", "Pets", "July", 2021, 1)
        self.database.writing_database("marsu", "expense", "Pets", "July", 2021, 3)

    def test_writing_database(self):
        self.rows = self.database.reading_database("marsu", "July", 2021)
        self.answer = [("marsu", "expense", "Pets", "July", 2021, 16)]
        self.assertEqual(self.rows, self.answer)