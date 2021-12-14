import unittest
from database_services.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.database.dcursor.execute('''DELETE FROM Database''')
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 12)
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 1)
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 3)

    def test_writing_database(self):
        rows = self.database.reading_database("marsu", 7, 2021)
        answer = [("marsu", "expense", "Pets", '7', 2021, 16)]
        self.assertEqual(rows[0], answer)
