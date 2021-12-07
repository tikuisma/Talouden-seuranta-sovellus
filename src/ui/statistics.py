from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import matplotlib
matplotlib.use('TkAgg')

class Statistics:
    def __init__(self, database, user, month, year):
        self.database = database
        self.user = user
        self.month = month
        self.year = year
        self.data = []
        self.categories = []
        '''Luodaan uusi ikkuna-näkymä, jossa käyttäjä näkee menojensa tilastot
        pylväsdiagrammina. Ilmoitetaan myös mikäli tilastoja ei löytynyt.'''
        self.window = Tk()
        self.window.title(f"Statistics")
        self.window.geometry("500x400+10+10")
        data_exists= self.data_handling()
        if data_exists:
            self.figure = Figure(figsize = (5, 5), dpi = 100)
            canvas = FigureCanvasTkAgg(self.figure, master = self.window)
            self.x_axis = self.figure.add_subplot(111)
            width = .35
            self.bars = self.x_axis.bar(self.categories, self.data, width)
            self.x_axis.bar_label(self.bars)
            self.x_axis.set_ylim(top=(max(self.data)+30))
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
        data = self.database.reading_database(self.user, self.month, self.year)
        if data == []:
            return False
        for row in data:
            self.data.append(row[5])
            self.categories.append(row[2])
        return True
