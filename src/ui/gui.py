from tkinter import *
from tkinter.ttk import Combobox
from database_services.database import Database
from ui.confirm_window import ConfirmingWindow

class GUI:
    """
    Pääkäyttöliittymän näkymä, jossa näkyvät talouden seurannan kulujen
    ja menon lisäys.
    Puuttuu: kulujen ja menojen listaukset näkymässä.
    """
    def __init__(self, user):
        self.user = user
        self.window = Tk()
        self.window.title(f"Account: {self.user}")
        self.window.geometry("500x400+10+10")
        self.lbl = Label(self.window, text="Personal economics")
        self.lbl.place(x = 175, y = 10)

        self.income_lbl = Label(self.window, text="Incomes:")
        self.income_lbl.place(x=50, y=55)
        self.add_income_button = Button(self.window, text="Save income",
        command=self.income)
        self.add_income_button.place(x=50, y=75)
        self.income_category = ("Salary", "Gift", "Investments", "Others")
        self.cb = Combobox(self.window, values= self.income_category)
        self.cb.place(x=50, y=105)

        self.add_expense_lbl = Label(self.window, text="Expences:")
        self.add_expense_lbl.place(x=300, y=55)
        self.add_expense_button = Button(self.window, text="Save expense",
        command=self.expense)
        self.add_expense_button.place(x=300, y=75)
        self.expense_category = ("Groceries","Residential expenses","Hobbies",
        "Pets","Shopping","Fun","Restaurants/bars","Investments")
        self.cb2 = Combobox(self.window, values= self.expense_category)
        self.cb2.place(x=300, y=105)
        
        self.total_lbl = Label(self.window, text= "Amount:")
        self.total_lbl.place(x=130, y=135)
        self.total_field = Entry(self.window, text="")
        self.total_field.place(x=130, y=155)

        self.month_lbl = Label(self.window, text="Month:")
        self.month_lbl.place(x=130, y=230)
        self.month_data = ("January","February","March","April","May","June",
        "July","August","September","Octobec","November","December")
        self.cb3 = Combobox(self.window, values= self.month_data)
        self.cb3.place(x=130, y=250)

        self.year_lbl = Label(self.window, text="Year:")
        self.year_lbl.place(x=130, y=185)
        self.year_data = (2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028,
        2029, 2030, 2031, 2032)
        self.cb4 = Combobox(self.window, values= self.year_data)
        self.cb4.place(x=130, y=205)

        self.pop_up_field = Label(self.window, text="")
        self.pop_up_field.place(x=75, y=5)
        
        self.window.mainloop()

    def income(self):
        '''Valittaessa käyttöliittymässä save income-nappula, annetaan tieto
        eteenpäin, että kyseessä on tulo.'''
        income_category = self.cb.get()
        self.saving_income_expense("income", income_category)

    def expense(self):
        '''Valittaessa käyttöliittymässä save expense-nappula, annetaan tieto
        eteenpäin, että kyseessä on meno.'''
        expense_category = self.cb2.get()
        self.saving_income_expense("expense", expense_category)

    def saving_income_expense(self, income_expense, category):
        '''Tarkistetaan, että käyttäjä on täyttänyt vaadittavat tiedot.'''
        invalid_pop_notice = '''Check that you have chosen all of 
        the categorys and added amount.'''
        amount_pop_notice = "Amount needs to be given with numbers."
        total = self.total_field.get()
        month = self.cb3.get()
        year = self.cb4.get()
        self.pop_up_field.destroy()
        if category == "" or total == "" or month == "" or year == "":
            self.pop_up_field = Label(self.window, text=invalid_pop_notice)
            self.pop_up_field.place(x=75, y=5)
        elif not total.isnumeric():
            self.pop_up_field = Label(self.window, text=amount_pop_notice)
            self.pop_up_field.place(x=75, y=5)
        else:
            '''Kutsutaan toista Oliota, jolle annetaan tiedot, jotta pystytään
            varmistamaan vielä tallennus tietokantaan.'''
            ConfirmingWindow(self.user, income_expense, category,
            month, year, total)