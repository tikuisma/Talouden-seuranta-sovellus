from services.log_in import *
from ui.gui import GUI
from ui.log_in_gui import LoginGUI

def main():
    """Pääfunktio, josta kutsutaan muita luokkia, metodeita ja funktioita.
    Args:
        Login: kutsutaan Log_in_GUI-luokkaa sisäänkirjautumisen
        mahdollistamiseksi.
    Returns:
        Signing in, jos sisäänkirjautuminen on onnistunut.
    Args:
        GUI: Kun sisäänkirjautuminen on onnistunut, kutsutaan päänäkymän
        avaavaa luokkaa.
    """
    Login = LoginGUI()
    if Login.pop_notice == "Signing in":
        GUI(Login.user)

if __name__ == "__main__":
    main()
