from tkinter import Label

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

        y_coordinate = 430
        text_class = Label(self.window, text= "Class",fg='black',
        font=('Arial',11,'bold'), anchor="w")
        text_class.place(x=40, y=y_coordinate)
        text_category = Label(self.window, text= "Category",fg='black',
        font=('Arial',11,'bold'), anchor="w")
        text_category.place(x=120, y=y_coordinate)
        text_month = Label(self.window, text= "Month",fg='black',
        font=('Arial',11,'bold'), anchor="w")
        text_month.place(x=270, y=y_coordinate)
        text_year = Label(self.window, text= "Year",fg='black',
        font=('Arial',11,'bold'), anchor="w")
        text_year.place(x=340, y=y_coordinate)
        text_amount = Label(self.window, text= "Amount",fg='black',
        font=('Arial',11,'bold'), anchor="w")
        text_amount.place(x=410, y=y_coordinate)

        data = self.database.reading_database_for_table(self.user)
        while len(data) < 5:
            data.append(("", "", "", "", ""))
        x_coord = [40, 120, 270, 340, 410]
        y_coord = 450
        for i in range(5):
            for j in range(len(data[0])):
                table = Label(self.window, text=data[i][j], width=20,
                fg='black', font=('Arial',10), anchor="w")
                table.place(x=x_coord[j], y=y_coord)
            y_coord += 20
