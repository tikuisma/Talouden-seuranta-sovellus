import unittest
from database_services.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.database.dcursor.execute('''DELETE FROM Database''')
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 12)
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 1)
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 3)

    def test_reading_database(self):
        rows = self.database.reading_database("marsu", 7, 2021)
        answer = [("marsu", "expense", "Pets", '7', 2021, 16)]
        self.assertEqual(rows[0], answer)
        answer2 = ([], [])
        self.assertEqual(self.database.reading_database("kirsikka", 7, 2021), answer2)

    def test_writing_database(self):
        self.database.writing_database("kerttu", "income", "Salary",
        12, 2021, 3000)
        reading = self.database.reading_database("kerttu", 12, 2021)
        answer = ([], [("kerttu", "income", "Salary", '12', 2021, 3000)])
        self.assertEqual(reading, answer)