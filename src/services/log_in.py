from database_services.user_database import UserDatabase

database = UserDatabase()
def new_user_creation(username):
    """Funktio, jonka avulla luodaan uusi käyttäjä ja tarkistetaan, että
    vaaditut käyttäjävaatimukset täyttyvät sekä luonnin onnistuessa,
    tallennetaan käyttäjänimi tietokantaan.

    Args:
        username: Syötetty käyttäjänimi käyttöliittymästä.

    Returns:
        Palauttaa käyttäjälle ilmoituksen käyttäjätunnuksen onnistumisesta
        tai epäonnistumisesta.
    """

    if database.user_doesnt_exists(username) and \
        len(username) <= 12 and len(username) >= 4:
        database.writing_database_username(username)
        return "Your account has been created. Next please log in."
    if not database.user_doesnt_exists(username):
        return "Username is already taken. Try another one."
    if len(username) > 12 or len(username) < 4:
        return "Check your usernames length requirements and try again."

def user_login(username):
    """Tarkistetaan sisäänkirjautumistila eli sisäänkirjautumisen onnistuminen
    käyttäjätunnuksella.

    Args:
        username: Syötetty käyttäjänimi käyttöliittymästä.

    Returns:
        Palauttaa viestin, mikäli sisäänkirjautuminen onnistui. Palauttaa
        viestin, mikäli käyttäjätunnusta ei löytynyt.
    """

    if database.user_doesnt_exists(username):
        return "User not found. Please check spelling or create new user."
    if not database.user_doesnt_exists(username):
        return "Signing in"
