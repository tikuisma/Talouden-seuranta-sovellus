from tkinter import Label, Button, Tk, Entry
from services.log_in import new_user_creation, user_login

class LoginGUI:
    """Luokka, jonka avulla luodaan käyttöliittymän sisäänkirjautumisnäkymä,
    jossa voi joko luoda käyttäjän ja/tai sisäänkirjautua.
    """

    def __init__(self):
        """Luokan konstruktori, joka sisäänkirjautumisikkunan.
        """

        self.user = ""
        self.log_in_screen = Tk()
        self.log_in_screen.title("Log in")
        self.log_in_screen.geometry("500x400+10+10")
        self.pop_notice = ""
        self.lbl = Label(self.log_in_screen, text="Enter your username:")
        self.lbl.place(x = 175, y = 50)
        self.username_field = Entry(self.log_in_screen, text="")
        self.username_field.place(x = 175, y = 75)
        self.log_in_button = Button(self.log_in_screen,
        text="Login", command=self.login)
        self.log_in_button.place(x = 220, y = 120)

        self.lbl2 = Label(self.log_in_screen,
        text='''Creating new user?\n Username length must be 4-12 marks.
        Write your username above to the open field
        and press "Create new user"-button.''')
        self.lbl2.place(x = 67, y = 200)
        self.new_user_button = Button(self.log_in_screen,
        text='''Create new user''',
        command=self.new_user)
        self.new_user_button.place(x = 175, y = 280)
        self.pop_up_field = Label(self.log_in_screen, text="")
        self.pop_up_field.place(x=125, y=100)

        self.log_in_screen.mainloop()

    def new_user(self):
        """Kutsuu toista funktiota, joka tarkistaa syötetyn käyttäjätunnuksen
        vaatimukset ja luo käyttäjätunnuksen, mikäli vaatimukset täyttyvät.
        """

        self.user = str(self.username_field.get())
        self.pop_notice = new_user_creation(self.user)

        """self.pop_notice: Palauttaa tiedon käyttäjälle graafisen
        käyttöliittymän sisäänkirjautumisnäkymään tekstin joko onnistuneesta
        käyttäjän luomisesta tai tämän epäonnistumisesta.
        """

        self.pop_up_field.destroy()
        self.pop_up_field = Label(self.log_in_screen, text=self.pop_notice)
        self.pop_up_field.place(x=125, y=100)

    def login(self):
        """Kutsutaan toista funktiota, joka tarkistaa löytyykö syötetty
        käyttäjänimi tietokannasta.

        Mikäli käyttäjänimi löytyy, sisäänkirjautumisikkuna suljetaan. Jos
        käyttäjänimeä ei löydy, käyttäjälle annetaan ilmoitus graafisessa
        käyttöliittymässä.
        """

        self.user = str(self.username_field.get())
        self.pop_up_field.destroy()
        self.pop_notice = user_login(self.user)
        if self.pop_notice == "Signing in":
            self.log_in_screen.destroy()
        else:
            self.pop_up_field = Label(self.log_in_screen, text=self.pop_notice)
            self.pop_up_field.place(x=115, y=100)
