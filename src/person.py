class Person:
    """
    Käyttäjän tietojen luokka.
    """
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return str(self.username)