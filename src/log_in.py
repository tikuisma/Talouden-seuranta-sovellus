from person import Person
users = {}
def new_user_creation(username): 
    """
    Luodaan uusi käyttäjä ja tarkistetaan, että käyttäjävaatimukset täyttyvät.
    Args: 
        username: Käyttäjänimi käyttöliittymästä.
    Returns:
        Palauttaa käyttöliittymän viestin siitä onnistuiko käyttäjätunnuksen luominen.
    """
    if username not in users and len(username) <= 12 and len(username) >= 4:
        users[username] = Person(username)
        return "Your account has been created. Next please log in."
    elif username in users:
        return "Username is already taken. Try another one."
    elif len(username) > 12 or len(username) < 4:
        return "Check your usernames length requirements and try again."

def user_login(username):
    """
    Tarkistetaan sisäänkirjautumistila eli sisäänkirjautumisen onnistuminen käyttäjätunnuksella.
    Args: 
        username: Käyttäjänimi käyttöliittymästä.
    Returns:
        Palauttaa tyhjän, mikäli onnistunut sisäänkirjautuminen. Palauttaa viestin, mikäli käyttäjätunnusta
        ei löytynyt.
    """
    if username not in users:
        return "User not found. Please check spelling or create new user."
    elif username in users:
        return ""