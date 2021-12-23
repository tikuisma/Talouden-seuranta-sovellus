import unittest
from tkinter import Tk
from ui.table import Table
from database_services.database import Database

class TestTable(unittest.TestCase):
    def setUp(self):
        self.database = Database()
        self.window = Tk()
        self.database.dcursor.execute('''DELETE FROM Database''')
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 12)
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 1)
        self.database.writing_database("marsu", "expense", "Pets", 7, 2021, 3)
        self.user = "marsu"
        self.table = Table(self.window, self.user, self.database)

    def test_creating_table(self):
        self.assertEqual(self.table.user, self.user)

    def test_database(self):
        self.assertEqual(self.table.database, self.database)
