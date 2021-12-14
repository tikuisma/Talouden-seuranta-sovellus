import unittest
from ui.statistics import Statistics
from database_services.database import Database
from tests.test_ui.test_tkinter import TestTkinter

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.database.dcursor.execute('''DELETE FROM Database''')
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 12)
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 1)
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 3)
        self.user = "marsu"
        self.month = 7
        self.year = 2021
        self.statistics = Statistics(self.database, self.user, self.month,
        self.year)
        self.window = TestTkinter()

    def test_data_handling(self):
        self.assertEqual(self.statistics.data_handling(), True)

