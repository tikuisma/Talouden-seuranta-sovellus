# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa tällä hetkellä kaksitasoista kerrosarkkitehtuuria ja pakkausrakenne on seuraava:
![IMG_20211223_193427__01](https://user-images.githubusercontent.com/93583969/147274701-3b53060f-5d54-45c0-83b9-43992041c266.jpg)
Pakkaus ui sisältää käyttöliittymästä, services sovelluksen backendia sisäänkirjautumiselle ja database_services tietojen pysyväistallennuksesta vastaavan koodin eli tietokantakutsuja. Data sisältää ohjelman tietokannat.

## Käyttöliittymä

Käyttöliittymä sisältää neljä erillistä näkymää:
- Sisäänkirjautuminen/uuden käyttäjän luominen.
- Päänäkymä, jossa pystyy lisäämään tuloja ja menoja. Siirtymään tilastojen katseluun.
- Varmistusnäkymä tulon/menon tallennukselle.
- Tilastonäkymä
Jokainen näkymä on toteutettu omana luokkana. Näkymistä yksi on aina kerrallaan käyttäjälle näkyvissä. UI-hakemisto vastaa näkymien näyttämisestä. 

Kun sovelluksen "päänäkymässä" päivitetään viisi viimeiseksi lisättyä tuloa/menoa, kutsutaan sovelluksen GUI-luokan metodia *income_expense_table*, joka taas edelleen kutsuu Table-luokkan metodia *creating_table*, joka sekä luo taulukon että päivittää sen uudelleen tietokannasta haettujen tietojen perusteella.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat ``UserDatabase``. ``Database`` ja ``log_in``-moduuli. Käyttöliittymää ohjaavat myös seuraavat luokat:``GUI``, ``LoginGUI``, ``ConfirmingWindow``, ``Table``, ``Statistics``.

Sovelluslogiikka muodostaa funktiot, joilla tarkistetaan käyttäjän luominen ja tämän lisääminen tai käyttäjän olemassaolo sisäänkirjautumista varten. 
Sovelluksen päänäkymä on tehty ``GUI``-luokkaan, joka sisältää metodeja, joilla kutsutaan ``Database``-luokkaa tai avataan uusia näkymiä.
``Statistics``-luokka luo uuden näkymän, jonka metodit kutsuvat ``Database``-luokkaa, joka taas palauttaa takaisin tiedot metodien käytettäviksi.
``Database``-luokka hallitsee yhteydenpitoa tietokannan kanssa eli se sisältää kaikki tietokantakutsut ja palauttaa käytettävässä muodossa tietoa muille luokille ja metodeille.

Tässä services-kansion ja sen liitoksissa olevan ohjelman muiden osien suhdetta kuvaava luokka/pakkauskaavio:

![IMG_20211214_202000__01](https://user-images.githubusercontent.com/93583969/146057272-97943cb3-8197-45f4-92b7-7c90901f273f.jpg)

## Tietojen pysyväistallennus
Tietojen pysyväistallennuksessa on käytetty ainoastaan SQL:n tietokantoja. Pakkauksen *database_services* luokat ``UserDatabase`` ja ``Database`` huolehtivat tietojen tallentamisesta. Molemmat luokat tallentavat tietonsa SQLite3-tietokantaan.

### Tiedostot

Sovellus tallentaa käyttäjät ja käyttäjien lisäämät tiedot eri tietokantoihin.
Sovelluksen juureen sijoitettu konfiguraatiotiedosto .env määrittelee tiedostojen nimet ja polut.
Käyttäjät tallennetaan SQLite3-tietokantatauluun ``Users``, joka alustetaan [user_database.py](https://github.com/tikuisma/ot-harjoitustyo/blob/master/src/database_services/user_database.py)-tiedostossa.
Käyttäjän tallentamat tiedot taas tallennetaan SQLite3-tietokantatauluun ``Database``, joka alustetaan [database.py](https://github.com/tikuisma/ot-harjoitustyo/blob/master/src/database_services/database.py)-tiedostossa.

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka yhden päätoiminnallisuuden osalta sekvenssikaaviona.

### Käyttäjän luominen ja sisäänkirjaantuminen

Kun kirjautumisnäkymän syötekenttään kirjoitetaan käyttäjätunnus, tämän jälkeen klikataan *Log in* -painiketta, etenee sovelluksen kontrolli seuraavasti:
![Sekvenssikaavio](https://user-images.githubusercontent.com/93583969/145101548-ba1e8c03-7423-4ab2-925e-fe460cb79202.jpg)
Ohjelman käynnistäessä main kutsuu ``LoginGUI``-luokkaa, joka luo graafisen käyttöliittymän. ``LoginGUI`` taas kutsuu *Log_in*-tiedoston *new_user_creation*-funktiota, jolle on annettu parametriksi käyttäjänimi. Sovelluslogiikka selvittää onko ``UserDatabase``:n avulla onko käyttäjänimi jo olemassa. Jos ei ole, käyttäjä palauttaa ilmoituksen onnistuneesta käyttäjänimen luonnista. Tämän jälkeen kutsutaan *user_login*-funktiota, jolla sovelluslogiikka tarkistaa onko käyttäjänimi olemassa, jos tämä löytyy, sisäänkirjautuminen onnistuu. Käyttöliittymä vaihtaa näkymäksi ``GUI``:n eli sovelluksen varsinaisen päänäkymän ja näyttää näkymään sisäänkirjautuneen käyttäjän mahdolliset lisäykset.

### Käyttäjän tulon tai menon lisääminen sekä tilaston lukeminen että taulukon luominen päänäkymään
![IMG_20211223_182534__01](https://user-images.githubusercontent.com/93583969/147267923-8994279a-bf2a-4cbb-9dd8-afd93738909b.jpg)

Kun käyttäjä haluaa tallentaa kuluja tai menoja valitsee hän vetovalikoista kategoriat ja syöttää summan. Kun käyttäjä painaa *save income* - tai *save expense* -nappulaa kutsutaan ``ConfirmingWindow``-luokkaa, jolle annetaan tiedot ja luokka luo uuden näkymän. Käyttäjän valitessa graafisessa käyttöliittymässä tallennuksen eli *check_save* -metodin. Kutsutaan ``Database``-luokan metodia *writing_database*, jolle annetaan tallennettavat tiedot. Tietokantaan tallennuksen jälkeen, ikkuna sulkeutuu ja palaudutaan takaisin ``GUI``-luokan luomaan ikkunanäkymään. Käyttäjän valitessa graafisessa käyttöliittymässä tilastojen etsintä -kohdan valitsemillaan tiedoilla kutsutaan ``Statistics``-luokkaa. Statistics-olio taas kutsuu ``Database``-luokan metodia *reading_database*, joka taas palauttaa löytämänsä tiedot takaisin ``Statistics``-luokalle, joka taas palauttaa ``GUI``-luokalle tiedon tietojen löytymisestä. Käyttäjän halutessa päivittää päänäkymän taulukon, ensin käyttäjä kutsuu graafisessa käyttöliittymässä luokan omaa metodia, *income_expense_table*, joka taas kutsuu ``Table``-luokan *creating_table*-metodia. ``Table``-luokan metodi taas kutsuu ``Database``-luokan metodia *reading_database_for_table*, joka palauttaa löytyneet tiedot takaisin ``Table``-luokan metodille käsiteltäväksi. ``Table``-luokka taas "palauttaa" valmistuttuaan ``GUI``-luokalle päivitetyn taulukon graafiseen käyttöliittymään. 

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä
Graafisen käyttöliittymän koodissa on hieman toisteisuutta, jota voisi poistaa luomalla metodeja esimerkiksi tekstien luomiselle. Koodia olisi myös mahdollisesti voinut jakaa hieman pienempiin osiin.
