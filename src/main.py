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

    okay = True
    while okay:
        okay = False
        login = LoginGUI()
        if login.pop_notice == "Signing in":
            okay = GUI(login.user)

if __name__ == "__main__":
    main()
