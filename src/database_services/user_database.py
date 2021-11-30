import sqlite3
class UserDatabase:
    def __init__(self):
        '''SQLite3:n tietokannan luonti'''
        self.database = sqlite3.connect('./users.db')
        self.dcursor = self.database.cursor()
        self.dcursor.execute('''CREATE TABLE IF NOT EXISTS
        Users (username TEXT)''')

    def writing_database_username(self, username):
        '''Saa usernamen ja tämä syötetään omaan tietokanta-tauluun.'''
        self.dcursor.execute('''INSERT INTO Users (username)
         VALUES (?)''', [username])
        self.database.commit()

    def user_doesnt_exists(self, username):
        '''Saa usernamen ja haetaan tieto onko username jo tietokannassa'''
        check = self.dcursor.execute('''SELECT username FROM Users''')
        rows = check.fetchall()
        if (username,) in rows:
            return False
        else:
            return True
