import sqlite3
import os.path
class Database:
    def __init__(self):
        '''Luodaan SQLite3:n tietokanta-taulu, johon merkitään username,
        income/expense, category, month, year ja amount'''
        self.database = sqlite3.connect('./database.db')
        self.dcursor = self.database.cursor()
        self.dcursor.execute('''CREATE TABLE IF NOT EXISTS Database
         (username TEXT,
         Income_Expense TEXT,
         Category TEXT,
         Month TEXT,
         Year INTEGER,
         Amount INTEGER)''')
    
    def writing_database(self, username, income_expense,
    category, month, year, amount):
        '''Viedään tietokantatauluun saadut tiedot.'''
        self.dcursor.execute('''INSERT INTO database
        (username,
        income_expense,
        category,
        month,
        year,
        amount)
        VALUES (?, ?, ?, ?, ?, ?)''',
        [username, income_expense, category, month, year, amount])
        self.database.commit()

    def reading_database(self): #ei vielä toiminnassa
        check = self.dcursor.execute('''SELECT * FROM Database''')
        rows = check.fetchall()
