from tkinter import Label
from tkinter.constants import LEFT

class Table:
    """Luokka, jonka avulla tehdään taulukko päänäkymään, jossa näkyy
    viisi viimeiseksi lisättyä menoa tai tuloa.

    Attributes:
        window: ohjelman pääikkunanäkymä.
        user: sisäänkirjautuneena oleva käyttäjänimi.
        database: tietokanta, jossa ovat käyttäjänimen lisäämät tiedot.
        """

    def __init__(self, window, user, database):
        """Luokan konstruktori

        Args:
            window: ohjelman pääikkunanäkymä.
            user: sisäänkirjautunut käyttäjänimi.
            database: tietokanta, jossa ovat käyttäjänimen lisäämät tiedot.
            """

        self.window = window
        self.user = user
        self.database = database

    def creating_table(self):
        """Luo taulukon tuloista/menoista päänäkymän alaosaan. Jos lisättyjä
        tuloja/menoja ei ole tietokannassa vielä viittä, lisätään taulukkoon
        tyhjiä kohtia.

        Args:
            database.reading_database_for_table: kutsutaan toisen luokan
            metodia, joka lukee tietokannasta käyttäjänimen mukaiset lisäykset.
        """

        data = self.database.reading_database_for_table(self.user)
        while len(data) < 5:
            data.append(("", "", "", "", ""))
        x_coord = [40, 120, 270, 320, 390]
        y_coord = 430
        for i in range(5):
            for j in range(len(data[0])):
                self.table = Label(self.window, text=data[i][j], width=20,
                fg='black', font=('Arial',10,'bold'), anchor="w")
                self.table.place(x=x_coord[j], y=y_coord)
            y_coord += 20
