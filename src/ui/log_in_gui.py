from tkinter import *
from tkinter.ttk import Combobox
from services.log_in import *

class Log_in_GUI:
    """
    Käyttöliittymän sisäänkirjautumisnäkymä, jossa voi joko luoda
    käyttäjän tai sisäänkirjautua.
    """
    def __init__(self):
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
        text="Log in", command=self.login)
        self.log_in_button.place(x = 220, y = 120)

        self.lbl2 = Label(self.log_in_screen,
        text='''Creating new user?\n Username length must be min. 4\
        and max. 12 marks.\n Write your username above to the open field
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
        """
        Kutsuu toista funktiota, joka luo käyttäjätunnuksen.
        """
        self.user = str(self.username_field.get())
        self.pop_notice = new_user_creation(self.user)
        
        """
        Palauttaa graafisen käyttöliittymän sisäänkirjautumisnäkymään tekstin.
        """
        self.pop_up_field.destroy()
        self.pop_up_field = Label(self.log_in_screen, text=self.pop_notice)
        self.pop_up_field.place(x=125, y=100)
      
    def login(self):
        self.user = str(self.username_field.get())
        self.pop_up_field.destroy()
        self.pop_notice = user_login(self.user)
        if self.pop_notice == "Signing in":
            self.log_in_screen.destroy()
        else:
            self.pop_up_field = Label(self.log_in_screen, text=self.pop_notice)
            self.pop_up_field.place(x=115, y=100)
