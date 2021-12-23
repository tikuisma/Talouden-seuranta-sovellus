from tkinter import Tk, Label, Button
from database_services.database import Database

database = Database()
class ConfirmingWindow:
    """Luokka, jonka avulla tehdään uusi ikkunanäkymä käyttäjälle, jossa
    varmistetaan tallennettava tieto vielä käyttäjältä.

    Attributes:
        username: Sisäänkirjautunut käyttäjä.
        income_expense: Tieto siitä onko tallennettava tulo vai meno.
        category: Tallennettavan tulon/menon valittu kategoria.
        month: Käyttäjän valitsema kuukausi.
        year: Käyttäjän valitsema vuosi.
        amount: Käyttäjän syöttämä summa.
    """

    def __init__(self, username, income_expense, category, month, year, amount):
        self.data = [username, income_expense, category, month, year, amount]
        """Luokan konstruktori, jolla luodaan uusi ikkunanäkymä.

        Args:
            username: Sisäänkirjautunut käyttäjä.
            income_expense: Tieto siitä onko tallennettava tulo vai meno.
            category: Tallennettavan tulon/menon valittu kategoria.
            month: Käyttäjän valitsema kuukausi.
            year: Käyttäjän valitsema vuosi.
            amount: Käyttäjän syöttämä summa.
        """

        self.window = Tk()
        self.window.title("Confirm?")
        self.window.geometry("450x200+10+10")
        self.lbl = Label(self.window, text="Confirming your information recording?")
        self.lbl.place(x=75, y=10)

        self.check_lbl = Label(self.window, text=
        '''Are you sure that you want to continue to save your options?
        To confirm your choices, you must press "Save" or
        if you dont want to save, please press "Don't save".''')
        self.check_lbl.place(x=18, y=40)

        self.save_button = Button(self.window,
        text="Save", command=self.check_save)
        self.save_button.place(x=80, y=100)

        self.cancel_button = Button(self.window,
        text="Don't save", command=self.dont_save)
        self.cancel_button.place(x=200, y=100)

        self.window.mainloop()

    def check_save(self):
        """Käyttäjän valitessa tietojen tallennus, kutsutaan toista funktiota,
        jolle annetaan tarvittavat tiedot, jotka siirretään tietokantaan.
        Tämän jälkeen ikkuna sulkeutuu ja palataan takaisin ns. pääikkunaan.
        """

        database.writing_database(self.data[0],self.data[1],
        self.data[2],self.data[3],self.data[4],self.data[5])
        self.window.destroy()

    def dont_save(self):
        """Mikäli käyttäjä ei haluakaan tallentaa tietoja. Ikkuna sulkeutuu ja
        palataan takaisin ns. pääikkunanäkymään.
        """

        self.window.destroy()
