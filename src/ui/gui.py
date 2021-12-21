from tkinter import Tk, Label, Entry, Button
from tkinter.ttk import Combobox
from database_services.database import Database
from ui.confirm_window import ConfirmingWindow
from ui.statistics import Statistics
from ui.table import Table

class GUI:
    """Luokka, joka luo ns. pääikkunanäkymän, jossa näkyvät sisäänkirjautuneen
    käyttäjän talouden seuranta.

    Attributes:
        user: sisäänkirjautunut käyttäjä.
    """

    def __init__(self, user):
        """Luokan konstruktori, joka luo ikkunanäkymän ja sille annetut tiedot.

        Args:
            user: sisäänkirjautunut käyttäjä.
        """

        self.user = user
        self.window = Tk()
        self.window.title(f"Account: {self.user}")
        self.window.geometry("500x630+10+10")
        self.lbl = Label(self.window, text="Personal economics")
        self.lbl.place(x = 175, y = 10)

        self.sign_out_button = Button(self.window, text="Sign out",
        command=self.sign_out)
        self.sign_out_button.place(x=380, y=10)

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
        "Pets","Shopping","Fun","Restaurants/bars")
        self.cb2 = Combobox(self.window, values= self.expense_category)
        self.cb2.place(x=300, y=105)

        self.total_lbl = Label(self.window, text= "Amount:")
        self.total_lbl.place(x=130, y=135)
        self.total_field = Entry(self.window, text="")
        self.total_field.place(x=130, y=155)

        self.month_lbl = Label(self.window, text="Month:")
        self.month_lbl.place(x=130, y=230)
        self.month_data = (1,2,3,4,5,6,7,8,9,10,11,12)
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

        self.statistics_lbl=Label(self.window, text='''Search your expense-statistics here:''')
        self.statistics_lbl.place(x = 100, y = 295)

        self.month_statistics_lbl = Label(self.window, text="Month:")
        self.month_statistics_lbl.place(x=50, y=320)
        self.month_statistics_data = (1,2,3,4,5,6,7,8,9,10,11,12)
        self.cb5 = Combobox(self.window, values= self.month_statistics_data)
        self.cb5.place(x=50, y=340)

        self.year_statistics_lbl = Label(self.window, text="Year:")
        self.year_statistics_lbl.place(x=250, y=320)
        self.year_statistics_data = (2021, 2022, 2023, 2024, 2025, 2026, 2027,
        2028, 2029, 2030, 2031, 2032)
        self.cb6 = Combobox(self.window, values= self.year_statistics_data)
        self.cb6.place(x=250, y=340)

        self.statistic_btn = Button(self.window, text="Go to statistics",
        command=self.statistics_button)
        self.statistic_btn.place(x=150, y=375)

        self.top5_btn = Button(self.window, text="Refresh latest",
        command=self.income_expense_table)
        self.top5_btn.place(x=150, y=550)

        self.income_expense_table()

        self.window.mainloop()

    def income(self):
        """Valittaessa graafisessa käyttöliittymässä save income-nappula,
        annetaan tieto eteenpäin, että kyseessä on tulo tietokantaan tallennusta
        varten.
        """

        income_category = self.cb.get()
        self.saving_income_expense("income", income_category)

    def expense(self):
        """Valittaessa graafisessa käyttöliittymässä save expense-nappula,
        annetaan tieto eteenpäin, että kyseessä on meno tietokantaan tallennusta
        varten.
        """

        expense_category = self.cb2.get()
        self.saving_income_expense("expense", expense_category)

    def saving_income_expense(self, income_expense, category):
        """Tarkistetaan, että käyttäjä on täyttänyt tulon/menon tallennusta
        varten vaaditut tiedot sekä nämä on täytetty oikein. Jos tietoja puuttuu
        tai niitä ei ole annettu oikein, käyttäjälle annetaan ilmoitus.

        Args:
            income_expense: tieto onko kyseessä tulon vai menon tallennus.
            category: mikä valittu kategoria on kyseessä tallennettavassa
            tulossa/menossa.
        """

        invalid_pop_notice = '''Check that you have chosen all of
        the categorys, added amount and you are clicking the right button.'''
        amount_pop_notice = '''Amount needs to be given with numbers.'''
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
            """Kutsutaan toista oliota, jolle annetaan tieto käyttäjästä,
            onko kyseessä tulo vai meno, valittu kategoria tulosta/menosta,
            valittu kuukausi ja vuosi sekä syötetty summa, jotta käyttäjälle
            voidaan avata uusi ns. varmistusikkuna.
            """

            ConfirmingWindow(self.user, income_expense, category,
            month, year, total)

    def statistics_button(self):
        """Valittujen kuukauden ja vuoden perusteella etsittävä tilastonäkymä.
        Jos käyttäjä ei ole valinnut oikein haettavaa tietoa, annetaan tästä
        ilmoitus. Muutoin kutsutaan toista oliota, joka luo tilastonäkymän.
        """

        st_month = self.cb5.get()
        st_year = self.cb6.get()
        invalid_pop_notice = "You need to give month and year for the search."
        if st_month == "" or st_year == "":
            self.pop_up_field = Label(self.window, text=invalid_pop_notice)
            self.pop_up_field.place(x=75, y=5)
        else:
            Statistics(Database(),self.user, st_month, st_year)

    def income_expense_table(self):
        """Kutsutaan toista oliota, jolle annetaan nykyinen ikkuna,
        sisäänkirjautunut käyttäjä sekä tietokanta-olio, jolla pystytään luomaan
        päänäkymään viisi viimeksi lisättyä menoa ja/tai tuloa.
        """

        table = Table(self.window, self.user, Database())
        table.creating_table()

    def sign_out(self):
        """
        """
        self.window.destroy()
