# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa tällä hetkellä kaksitasoista kerrosarkkitehtuuria ja pakkausrakenne on seuraava:
![Arkkitehtuuri](https://user-images.githubusercontent.com/93583969/144111773-7ddebc2b-4b6f-4352-8d4e-dd7e0f152779.jpg)
Pakkaus ui sisältää käyttöliittymästä, services sovelluksen backendia sisäänkirjautumiselle ja database_services tietojen pysyväistallennuksesta vastaavan koodin eli tietokantakutsuja.

## Käyttöliittymä

Käyttöliittymä sisältää neljä erillistä näkymää:
- Sisäänkirjautuminen/uuden käyttäjän luominen
- Päänäkymä, jossa pystyy lisäämään tuloja ja menoja. Siirtymään tilastojen katseluun.
- Varmistusnäkymä tulon/menon tallennukselle.
- Tilastonäkymä
Jokainen näkymä on toteutettu omana luokkana. Näkymistä yksi on aina kerrallaan käyttäjälle näkyvissä. UI-hakemisto vastaa näkymien näyttämisestä. 

## Sovelluslogiikka

Sovelluslogiikka muodostaa funktiot, joilla tarkistetaan käyttäjän luominen ja tämän lisääminen tai käyttäjän olemassaolo sisäänkirjautumista varten. 
Sovelluksen päänäkymä on tehty GUI-luokkaan, joka sisältää metodeja, joilla kutsutaan Database-luokkaa tai avataan uusia näkymiä.
Statistics-luokka luo uuden näkymän, jonka metodit kutsuvat Database-luokkaa, joka taas palauttaa takaisin tiedot metodien käytettäviksi.
Database-luokka hallitsee yhteydenpitoa tietokannan kanssa eli se sisältää kaikki tietokantakutsut ja palauttaa käytettävässä muodossa tietoa muille luokille ja metodeille.


## Tietojen pysyväistallennus

Pakkauksen **database_services** luokat ``UserDatabase`` ja ``Database`` huolehtivat tietojen tallentamisesta. Molemmat luokat tallentavat tietonsa SQLite3-tietokantaan.

### Tiedostot

Sovellus tallentaa käyttäjät ja käyttäjien lisäämät tiedot eri tietokantoihin.
Sovelluksen juureen sijoitettu konfiguraatiotiedosto .env määrittelee tiedostojen nimet ja polut ???????
Käyttäjät tallennetaan SQLite3-tietokantatauluun ``Users``, joka alustetaan [user_database.py](https://github.com/tikuisma/ot-harjoitustyo/blob/master/src/database_services/user_database.py)-tiedostossa.
Käyttäjän tallentamat tiedot taas tallennetaan SQLite3-tietokantatauluun ``Database``, joka alustetaan [database.py](https://github.com/tikuisma/ot-harjoitustyo/blob/master/src/database_services/database.py)-tiedostossa.

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka yhden päätoiminnallisuuden osalta sekvenssikaaviona.

### Käyttäjän luominen ja sisäänkirjaantuminen

Kun kirjautumisnäkymän syötekenttään kirjoitetaan käyttäjätunnus, tämän jälkeen klikataan Log-in -painiketta, etenee sovelluksen kontrolli seuraavasti:
![Sekvenssikaavio](https://user-images.githubusercontent.com/93583969/145101548-ba1e8c03-7423-4ab2-925e-fe460cb79202.jpg)
Ohjelman käynnistäessä main kutsuu Log_in_GUI-luokkaa, joka luo graafisen käyttöliittymän. Log_in_GUI taas kutsuu Log_in-tiedoston new_user_creation-funktiota, jolle on annettu parametriksi käyttäjänimi. Sovelluslogiikka selvittää onko ``UserDatabase``:n avulla onko käyttäjänimi jo olemassa. Jos ei ole, käyttäjä palauttaa ilmoituksen onnistuneesta käyttäjänimen luonnista. Tämän jälkeen kutsutaan user_login-funktiota, jolla sovelluslogiikka tarkistaa onko käyttäjänimi olemassa, jos tämä löytyy, sisäänkirjautuminen onnistuu. Käyttöliittymä vaihtaa näkymäksi ``GUI``:n eli sovelluksen varsinaisen päänäkymän ja näyttää näkymään sisäänkirjautuneen käyttäjän mahdolliset lisäykset.

### Käyttäjän tulon tai menon lisääminen


