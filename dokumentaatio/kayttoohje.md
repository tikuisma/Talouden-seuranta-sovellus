# Käyttöohje

Lataa projektin viimeisin releasen lähdekoodi valitsemalla *Assets*-osion alta *Source code*.

## Konfigurointi

Tallennukseen käytettävien tiedostojen nimiä voi halutessaan konfiguroida käynnistyshakemistossa *.env*-tiedostossa. Tiedostot luodaan automaattisesti *data*-hakemistoon, mikäli nämä sieltä vielä puuttuvat. Tiedostojen muodot ovat seuraavat:
``DATABASE_FILE='database.db'``
``USERDATABASE_FILE='users.db'``

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
``poetry install``

Projektissa ei ole muita alustustoimenpiteitä, joten voit käynnistää sovelluksen komennolla:
``poetry run invoke start``

## Uuden käyttäjän luominen ja sisäänkirjautuminen

Sovellus käynnistyy kirjautumisnäkymään:

![sisäänkirjautuminen](https://user-images.githubusercontent.com/93583969/146052369-349ce2a4-0237-4c15-b01e-7373992ee389.png)

Mikäli sinulla on olemassa oleva käyttäjätunnus, syötetään se syötekenttään ja painamalla "Login"-painiketta.

![uusikäyttäjä](https://user-images.githubusercontent.com/93583969/146052426-0efb385c-955f-4faf-9c4d-947c44bd43d0.png)

Mikäli haluat luoda uuden käyttäjätunnuksen, syötetään haluttu käyttäjätunnus syötekenttään ja painetaan "Create new user"-painiketta. Tämän jälkeen saat ilmoituksen joko onnistuneesta tai epäonnistuneesta käyttäjän luomisesta. Mikäli käyttäjätunnuksen luonti onnistui, voit painaa "Login"-painiketta sisäänkirjautuaksesi ja päänäkymään päästäksesi.

## Päänäkymä

Onnistuneen sisäänkirjautumisen jälkeen avautuu päänäkymä:

![Screenshot from 2021-12-23 18-22-22](https://user-images.githubusercontent.com/93583969/147267249-98a4b5cd-ba58-45cd-8915-99c902e64d4a.png)

Tässä voi lisätä vetovalikoista tulon tai menon kategorian, syöttää sille summan, valita vuoden ja kuukauden sekä tämän jälkeen painaa joko "save income"- tai "save expense"-painiketta riippuen kumpaa ollaan tallentamassa, tästä avautuu uusi tallentamisen varmistus -näkymä.

![saveincome](https://user-images.githubusercontent.com/93583969/146052676-6b045501-4e96-4097-b356-2370317c8d32.png)

Mikäli haluat etsiä valitsemallasi kuukaudella ja vuodella lisätyt tulot ja menot, näet ne "Go to statistics" -painiketta painamalla, jolloin avautuu uusi näkymä.

### Tallentamisen varmistus -näkymä

Kun päänäkymässä on täydetty vaadittavat tiedot ja painettu jompaa kumpaa tallennus-painiketta, avautuu uusi näkymä.

![Screenshot from 2021-12-23 18-22-48](https://user-images.githubusercontent.com/93583969/147267207-675974dc-67a4-4353-973c-960d442e471c.png)

Tässä varmistetaan, että halutaan aiemmassa ikkunassa olleet tiedot tallentaa. Mikäli tiedot halutaan tallentaa, painetaan "Save" tai, jos halutaan palata takaisin tallentamatta, painetaan "Dont save"-painiketta.

Onnistuneen tulon/menon tallentamisen jälkeen palaudutaan takaisin päänäkymään, jossa voi painaa "Refresh latest", jolloin päänäkymään ilmestyy taulukko, josta näkee viimeisimmät viisi tuoreinta lisäystä.

![päivitetty varmistuksen jälkeen](https://user-images.githubusercontent.com/93583969/146052725-6c555d12-2ba9-44c8-bd71-743a05d93906.png)

### Tilastonäkymä

Kun päänäkymässä on täytetty vaadittavat tiedot ja painettu "Go to statistics" -painiketta, avautuu uusi näkymä, jossa näkyy sen kuukauden ja vuoden menot ja tulot.

![tilastonäkymä](https://user-images.githubusercontent.com/93583969/146052797-6bc5fff6-8b31-4234-8bc2-ac873fb9be55.png)

Mikäli näitä ei olisi, ikkuna avautuu ja ilmoittaa käyttäjälle viestillä, että tietoja ei löytynyt.

### Uloskirjautuminen

Päänäkymän oikeassa ylänurkassa on sign out -nappula. Tätä painamalla käyttäjä uloskirjautuu ja palaudutaan takaisin sisäänkirjautumisnäkymään.
