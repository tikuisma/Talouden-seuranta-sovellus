from tkinter import *
from database_services.database import Database

database = Database()
class ConfirmingWindow:
    def __init__(self, username, income_expense, category, month, year, amount):
        self.data = [username, income_expense, category, month, year, amount]
        '''Luodaan uusi näkymä, jossa varmistetaan käyttäjän tekemät
        tallennukset ennen tietokantaan siirtoa.'''
        self.window = Tk()
        self.window.geometry("500x400+10+10")
        self.lbl = Label(self.window, text='''Confirming your\
        information recording''')
        self.lbl.place(x=15, y=10)

        self.check_lbl = Label(self.window, text=
        '''Are you sure that you want to continue to save your options?
        To confirm your choices, you must press "Save" or
        if you dont want to save please press "Don't save".''')
        self.check_lbl.place(x=15, y=40)

        self.save_button = Button(self.window,
        text="Save", command=self.check_save)
        self.save_button.place(x=80, y=100)

        self.cancel_button = Button(self.window,
        text="Don't save", command=self.dont_save)
        self.cancel_button.place(x=200, y=100)

        self.window.mainloop()
    
    def check_save(self):
        '''Tätä metodia painettaessa, kutsutaan toista funktiota,
        johon annetaan tiedot, jotka viedään tietokantaan. Tämän jälkeen
        ikkuna sulkeutuu.'''
        database.writing_database(self.data[0],self.data[1],
        self.data[2],self.data[3],self.data[4],self.data[5])
        self.window.destroy()

    def dont_save(self):
        '''Painettaessa ei-tallentavaa -painiketta, näkymä poistuu.'''
        self.window.destroy()


