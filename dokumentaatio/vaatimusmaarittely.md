# Vaatimusmäärittely
_____________________

## Sovelluksen käyttötarkoitus
Sovelluksella käyttäjät pystyvät pitämään kirjaa tuloista ja menoista eli tarkoituksena on pitää kirjaa käyttäjän taloudesta. Sovellusta on mahdollista käyttää useampi käyttäjä, mutta jokaisella on oma käyttäjätunnus. 


## Käyttäjät
Sovelluksen käyttäjänä olisi tarkoitus toimia vain yksi käyttäjärooli eli ns. normaali käyttäjä. 


## Käyttöliittymäluonnos
Sovellus koostuu viidestä eri näkymästä, luonnos:

Sovelluksen käynnistäessä olisi ensin tarkoitus tulla käyttäjän kirjautumisnäkymä, jonka jälkeen jo rekisteröitynyt käyttäjä laittaa käyttäjätunnuksena ja kirjautuu sisään tai rekisteröimätön käyttäjä ensin rekisteröityy ja sitten kirjautuu sisään juuri luomallaan tunnuksella. Kirjautumisen jälkeen käyttäjälle avautuu näkymä, jossa on listattuna tulot, menot ja tilastot. Näistä tuloihin ja menoihin käyttäjä saa vetolaatikosta valita itselleen sopivan kategorian ja lisätä kuukauden sekä vuoden ja laittaa summan. Tilastoista nähdään kuukausittainen balanssi eli tulojen ja menojen yhteensovitus sekä kategoriat joihin rahaa on kulunut kuukauden aikana.


##Sovelluksen toiminnallisuus
###Sisäänkirjautuminen
- Käyttäjä luo järjestelmään käyttäjätunnuksen
	- käyttäjätunnus pitää olla vähintään 4 merkkiä pitkä ja maksimissaan 12 merkkiä
	- rekisteröitäessä uutta käyttäjätunnusta tarkistetaan ettei järjestelmässä ole jo vastaavaa käyttäjää eli jokainen käyttäjätunnus pitää olla erilainen
- Käyttäjän kirjautuminen sovellukseen
	- mikäli käyttäjällä on jo olemassa oleva käyttäjätunnus, kirjautuminen onnistuu syöttämällä tämän kirjautumisnäkymässä
	- jos käyttäjää ei löydy järjestelmästä, tästä tulee ilmoitus näytölle

###Onnistuneen sisäänkirjautumisen jälkeen
- Käyttäjälle aukeaa näkymä, jossa on listattuna Tulot, Menot, Tilastot ja Kirjaudu ulos -kohdat. Näistä valitsemalla "lisää tulo" tai "lisää meno", käyttäjä pääsee seuraavaan näkymään.
	- Valittaessa tulot, käyttäjä voi lisätä uuden tulon, nimetä sen ja asettaa summan.
	- Valittaessa menot, käyttäjä voi lisätä uuden menon, nimetä sen ja asettaa summan.
	- Tilastot ovat näkyvissä ns. päänäkymässä yhdessä tulojen ja menojen kanssa, käyttäjä näkee kuukausittaisen kulutuksensa, tässä näkyy saadut tulot ja menot kuukausittain sekä näiden tasapaino ja mihin kategorioihin rahaa on mennyt. 
	- Valittaessa Kirjaudu ulos, käyttäjä kirjautuu ulos järjestelmästä.
	- Kaikki käyttäjän tekemät muokkaukset tallennetaan heti, kun niihin on tehty muutoksia.
	- Päänäkymässä tulisi näkyä suunnilleen n. 10 viimeisintä lisäystä tuloihin/menoihin ja kuukauden vaihtuessa, nämä nollaantuvat.

###Jatkokehitysideat
- Ajan salliessa sovellusta olisi tarkoitus kehittää seuraavasti:
	- Tilastoja voisi tarkastella vuositasolla
	- Syöttäessä virheellisen tulon tai menon, tämän poistaminen
	- Päivämäärät esim. lisätessä menoja
	- Päänäkymästä pystyisi siirtymään osioon, jossa näkyisi kaikki asetetut tulot ja menot aikajärjestyksessä.
