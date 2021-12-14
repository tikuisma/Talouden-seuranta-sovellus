import sqlite3
from config import DATABASE_FILE_PATH

class Database:
    """Luokka, jonka avulla luodaan tietokanta käyttäjän syöttämistä tuloista
    ja menoista.
    """

    def __init__(self):
        """Luokan konstruktori, jolla luodaan SQLite3:n tietokanta-taulu, jonne
        annetaan käyttäjän syöttämät tiedot.
        """

        self.database = sqlite3.connect(DATABASE_FILE_PATH)
        self.dcursor = self.database.cursor()
        self.dcursor.execute('''CREATE TABLE IF NOT EXISTS Database
         (username TEXT,
         Income_Expense TEXT,
         Category TEXT,
         Month INTEGER,
         Year INTEGER,
         Amount INTEGER)''')

    def writing_database(self, username, income_expense,
    category, month, year, amount):
        """Lisätään tietokantaan käyttäjän syöttämät tiedot.

        Args:
            username: Sisäänkirjautunut käyttäjä.
            income_expense: Tieto onko kyseessä tulo vai meno.
            category: Tieto käyttäjän valitsemasta kategoriasta.
            month: Käyttäjän valitsema kuukausi.
            year: Käyttäjän valitsema vuosi.
            amount: Käyttäjän syöttämä summa.
        """

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
        """Luetaan tietokannasta annetuilla tiedoilla täsmäävät asiat.

        Args:
            user: Sisäänkirjautunut käyttäjä.
            month1: Käyttäjän valitsema kuukausi.
            year1: Käyttäjän valitsema vuosi.

        Returns:
            Tietokannasta saadut tiedot sekä menoista että tuloista listoina.
        """

        data_expense = self.dcursor.execute(f'''SELECT username,
        Income_Expense, Category, Month, Year, SUM(Amount) FROM Database
        WHERE income_expense = "expense" AND username = "{user}" AND
        Month = {month1} AND year = {year1} GROUP BY category''')
        rows_expense = data_expense.fetchall()

        data_income = self.dcursor.execute(f'''SELECT username,
        Income_Expense, Category, Month, Year, SUM(Amount) FROM Database
        WHERE income_expense = "income" AND username = "{user}" AND
        Month = {month1} AND year = {year1} GROUP BY category''')
        rows_income = data_income.fetchall()

        return rows_expense, rows_income

    def reading_database_for_table(self, user):
        """Luetaan tietokannasta sisäänkirjautuneen käyttäjän tiedot.

        Args:
            user: Sisäänkirjautunut käyttäjä.

        Returns:
            Tiedot käyttäjän tallentamista tiedoista tietokantaan tuoreimmasta
            vanhaan.
        """

        data = self.dcursor.execute(f'''SELECT Income_Expense, Category,
        Month, Year, Amount FROM Database WHERE username = "{user}" ORDER
        BY Year DESC, Month DESC''')
        row = data.fetchall()

        return row
