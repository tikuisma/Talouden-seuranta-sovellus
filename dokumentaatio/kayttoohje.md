# Käyttöohje

## Konfigurointi

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
``poetry install``

Tämän jälkeen ohjelman voi käynnistää komennolla:
``poetry run invoke start``

## Uuden käyttäjän luominen ja sisäänkirjautuminen

Sovellus käynnistyy kirjautumisnäkymään:

![sisäänkirjautuminen](https://user-images.githubusercontent.com/93583969/146052369-349ce2a4-0237-4c15-b01e-7373992ee389.png)

Mikäli sinulla on olemassa oleva käyttäjätunnus, syötetään se syötekenttään ja painamalla "Login"-painiketta.

![uusikäyttäjä](https://user-images.githubusercontent.com/93583969/146052426-0efb385c-955f-4faf-9c4d-947c44bd43d0.png)

Mikäli haluat luoda uuden käyttäjätunnuksen, syötetään haluttu käyttäjätunnus syötekenttään ja painetaan "Create new user"-painiketta. Tämän jälkeen saat ilmoituksen joko onnistuneesta tai epäonnistuneesta käyttäjän luomisesta. Mikäli käyttäjätunnuksen luonti onnistui, voit painaa "Login"-painiketta sisäänkirjautuaksesi ja päänäkymään päästäksesi.

## Päänäkymä

Onnistuneen sisäänkirjautumisen jälkeen avautuu päänäkymä:

Tässä voi lisätä vetovalikoista tulon tai menon, syöttää sille summan, valita vuoden ja kuukauden sekä tämän jälkeen painaa joko "save income"- tai "save expense"-painiketta riippuen kumpaa ollaan tallentamassa, tästä avautuu uusi tallentamisen varmistus -näkymä.
Onnistuneen tulon/menon tallennuksen jälkeen voi painaa "Refresh latest", jolloin päänäkymään ilmestyy taulukko, josta näkee viimeisimmät viisi tuoreinta lisäystä.
Mikäli haluat etsiä valitsemallasi kuukaudella ja vuodella lisätyt tulot ja menot, näät ne "Go to statistics" -painiketta painamalla, jolloin avautuu uusi näkymä.

### Tallentamisen varmistus -näkymä

Kun päänäkymässä on täydetty vaadittavat tiedot ja painettu jompaa kumpaa tallennus-painiketta, avautuu uusi näkymä.

Tässä varmistetaan, että halutaan aiemmassa ikkunassa olleet tiedot tallentaa. Mikäli tiedot halutaan tallentaa, painetaan "Save" tai, jos halutaan palata takaisin tallentamatta, painetaan "Dont save"-painiketta.

### Tilastonäkymä

Kun päänäkymässä on täytetty vaadittavat tiedot ja painettu "Go to statistics" -painiketta, avautuu uusi näkymä, jossa näkyy sen kuukauden ja vuoden menot ja tulot.

Mikäli näitä ei olisi, ikkuna avautuu ja ilmoittaa käyttäjälle viestillä, että tietoja ei löytynyt.

