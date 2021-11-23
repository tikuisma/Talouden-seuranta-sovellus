from tkinter import *
from tkinter.ttk import Combobox
class GUI:
    """
    Pääkäyttöliittymän näkymä, jossa näkyvät talouden seurannan kulujen ja menon lisäys.
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
        self.income_lbl.place(x = 50, y = 55)
        self.add_income_button = Button(self.window, text="Save income") # Ei vielä toiminnassa
        self.add_income_button.place(x = 50, y = 75)
        income_data = ("Salary", "Gift", "Investments", "Others")
        cb = Combobox(self.window, values= income_data)
        cb.place(x = 50, y = 105)

        self.add_expense_lbl = Label(self.window, text="Expences:")
        self.add_expense_lbl.place(x = 300, y = 55)
        self.add_expense_button = Button(self.window, text="Save expense") # Ei vielä toiminnassa
        self.add_expense_button.place(x = 300, y = 75)
        expense_data = ("Groceries", "Residential expenses", "Hobbies", "Pets", "Shopping", "Fun", "restaurants/bars", "Investments")
        cb2 = Combobox(self.window, values= expense_data)
        cb2.place(x = 300, y = 105)
        
        self.month_lbl = Label(self.window, text="Month:")
        self.month_lbl.place(x = 130, y = 135)
        month_data = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "Octobec", "November", "December")
        cb3 = Combobox(self.window, values= month_data)
        cb3.place(x = 130, y = 155)

        self.year_lbl = Label(self.window, text="Year:")
        self.year_lbl.place(x = 130, y = 185)
        year_data = ("2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032")
        cb4 = Combobox(self.window, values= year_data)
        cb4.place(x = 130, y = 205)
        
        self.window.mainloop()