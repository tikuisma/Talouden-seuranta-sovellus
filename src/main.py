from person import Person
from log_in import *
from GUI import *
from Log_in_GUI import *

def Main(): #kutsutaan funktioita, päätietokantakutsut ym.
    Login = Log_in_GUI()
    if Login.pop_notice == "":
        GUI(Login.user)

#Tietokannat vielä puuttuvat

if __name__ == "__main__":
    Main()