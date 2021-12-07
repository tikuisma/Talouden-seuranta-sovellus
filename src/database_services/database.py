import sqlite3
from config import DATABASE_FILE_PATH
class Database:
    def __init__(self):
        '''Luodaan SQLite3:n tietokanta-taulu, johon merkitään username,
        income/expense, category, month, year ja amount'''
        self.database = sqlite3.connect(DATABASE_FILE_PATH)
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

    def reading_database(self, user, month1, year1):
        data = self.dcursor.execute(f'''SELECT username,
        Income_Expense, Category, Month, Year, SUM(Amount) FROM Database
        WHERE income_expense = "expense" AND username = "{user}" AND
        Month = "{month1}" AND year = {year1} GROUP BY category''')
        rows = data.fetchall()
        return rows
