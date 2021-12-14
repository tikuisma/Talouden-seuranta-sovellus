import sqlite3
from config import USERDATABASE_FILE_PATH

class UserDatabase:
    """Luokka, jonka avulla luodaan tietokanta sovelluksen käyttäjistä.
    """

    def __init__(self):
        """Luokan konstruktori, jossa käytetään SQLite3:sta tietokannan
        luomisessa.
        """

        self.database = sqlite3.connect(USERDATABASE_FILE_PATH)
        self.dcursor = self.database.cursor()
        self.dcursor.execute('''CREATE TABLE IF NOT EXISTS
        Users (username TEXT)''')

    def writing_database_username(self, username):
        """Tallennetaan saatu käyttäjänimi tietokantaan.

        Args:
            username: Syötetty käyttäjänimi.
        """

        self.dcursor.execute('''INSERT INTO Users (username)
         VALUES (?)''', [username])
        self.database.commit()

    def user_doesnt_exists(self, username):
        """Tarkistetaan löytyykö käyttäjä jo tietokannasta.

        Args:
            username: Syötetty käyttäjänimi.

        Returns:
            False, jos käyttäjänimi löytyy tietokannasta, muussa tapauksessa
            True.
        """

        check = self.dcursor.execute('''SELECT username FROM Users''')
        rows = check.fetchall()
        if (username,) in rows:
            return False
        return True
