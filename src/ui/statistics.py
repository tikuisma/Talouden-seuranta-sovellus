from tkinter import Tk, Label
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import matplotlib
matplotlib.use('TkAgg')

class Statistics:
    """Luokka, jonka avulla luodaan ikkuna-näkymä, jossa käyttäjä näkee
    tulojensa ja menojensa tilastot pylväsdiagrammina. Ilmoitetaan myös mikäli
    tilastoja ei löytynyt.

    Attributes:
        database: Tietokanta, josta saadaan käyttäjän tiedot.
        user: Käyttäjä, joka on sisäänkirjautuneena.
        month: Käyttäjän valitsema kuukausi.
        year: Käyttäjän valitsema vuosi.
    """

    def __init__(self, database, user, month, year):
        """Luokan konstruktori, joka luo uuden ikkunanäkymän ja piirtää
        tilastograafin.

        Args:
            database: Tietokanta, josta saadaan käyttäjän lisäämät tiedot.
            user: Käyttäjä, joka on sisäänkirjautuneena.
            month: Käyttäjän valitsema kuukausi, josta etsitään tietoja.
            year: Käyttäjän valitsema vuosi, josta etsitään tietoja.
        """

        self.database = database
        self.user = user
        self.month = month
        self.year = year
        self.data = []
        self.categories = []
        self.window = Tk()
        self.window.title(f"Statistics")
        self.window.geometry("700x500+10+10")

        data_exists = self.data_handling()
        if data_exists:
            self.figure = Figure(figsize = (50, 50), dpi = 100)
            canvas = FigureCanvasTkAgg(self.figure, master = self.window)
            self.x_axis = self.figure.add_subplot(111)
            width = 0.5
            self.bars = self.x_axis.bar(self.categories, self.data, width)
            self.x_axis.bar_label(self.bars)
            self.x_axis.set_ylim(top=(max(self.data)+30))
            self.x_axis.axhline(0, color="black")
            canvas.draw()
            canvas.get_tk_widget().pack()
            toolbar = NavigationToolbar2Tk(canvas, self.window)
            toolbar.update()
            canvas.get_tk_widget().pack()
        else:
            self.data_lbl = Label(self.window, text= '''No data found. Please
            try different month or/and year.''')
            self.data_lbl.place(x=75, y=125)
        self.window.mainloop()

    def data_handling(self):
        """Ikkunaa luodessa tarkistetaan löytyykö käyttäjän valitsemalta
        kuukaudelta ja vuodelta tietokannasta mitään tietoja. Jos tietoja ei
        löydy, käyttäjälle tulee ikkunaan tästä ilmoitus.

        Returns:
            False, jos tietokannasta ei löydy valituilta kuukaudelta ja vuodelta
            tietoja. Muussa tapauksessa palautetaan True, ja ikkunaan piirretään
            pylväsdiagrammi käyttäjän lisäämien tietojen mukaan.
        """

        dataexpense, dataincome = self.database.reading_database(self.user, self.month, self.year)
        if dataexpense == [] and dataincome == []:
            return False
        for row in dataincome:
            self.data.append(row[5])
            self.categories.append(row[2])
        for row in dataexpense:
            self.data.append(-row[5])
            self.categories.append(row[2])
        return True
