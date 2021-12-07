from services.log_in import *
from ui.gui import *
from ui.log_in_gui import *

def main():
    '''Kutsutaan funktioita'''
    Login = Log_in_GUI()
    if Login.pop_notice == "Signing in":
        GUI(Login.user)

if __name__ == "__main__":
    main()
