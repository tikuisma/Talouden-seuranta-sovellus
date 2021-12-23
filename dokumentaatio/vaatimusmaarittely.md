# Vaatimusmäärittely
_____________________

## Sovelluksen käyttötarkoitus
Sovelluksella käyttäjät pystyvät pitämään kirjaa tuloista ja menoista eli tarkoituksena on pitää kirjaa käyttäjän taloudesta. Sovellusta on mahdollista käyttää useampi käyttäjä, mutta jokaisella on oma käyttäjätunnus, joilla kirjautua sovellukseen sisään. 


## Käyttäjät
Sovelluksen käyttäjänä olisi tarkoitus toimia vain yksi käyttäjärooli eli ns. normaali käyttäjä. 


## Käyttöliittymäluonnos
Sovellus koostuu kolmesta eri näkymästä, suuntaa antava luonnos ohessa:
![IMG_20211222_190531__01](https://user-images.githubusercontent.com/93583969/147267589-fe2befd2-42dd-46f8-8a0f-a6e537fb1dca.jpg)

Sovelluksen käynnistäessä olisi ensin tarkoitus tulla käyttäjän kirjautumisnäkymä, jonka jälkeen jo rekisteröitynyt käyttäjä laittaa käyttäjätunnuksensa ja kirjautuu sisään tai rekisteröimätön käyttäjä ensin rekisteröityy ja sitten kirjautuu sisään juuri luomallaan tunnuksella. Tässä näkymässä pystyy siis luomaan sekä käyttäjän että jo luotu käyttäjä pystyy sisäänkirjautumaan. Kirjautumisen jälkeen käyttäjälle avautuu näkymä, jossa käyttäjä voi lisätä itselleen menon ja/tai tulon. Kun käyttäjä haluaa tallentaa tulon/menon, ilmestyy näkyviin vielä uusi näkymä, jossa käyttäjältä varmistetaan haluttu tallennus. Tällä yritetään minimoida käyttäjän tekemät vahinkopainallukset sekä antaa käyttäjälle vielä mahdollisuus tarkistaa tiedot, joita ollaan tallentamassa. Tuloihin ja menoihin käyttäjä saa ennen tallentamista valita vetolaatikoista itselleen sopivan kategorian, lisätä kuukauden sekä vuoden ja laittaa summan. Kaikki kohdat tulee täyttää, muutoin sovellus ei anna käyttäjän tallentaa tietoja. Ns. päänäkymässä on vielä alle listattu 5 tuoreinta lisäystä. Mikäli käyttäjä lisäilee menoja/tuloja, voi käyttäjä painaa refresh-nappia, jolloin viisi viimeisintä lisättyä tulevat näkyviin sekä lisäysten jälkeen listauksen saa päivitettyä. Tilastoihin mentäessä käyttäjä valitsee ensin kuukauden ja vuoden, jolta haluaa nähdä kuukausittaisen menonsa ja tulonsa. Tästä aukeaa uusi näkymä ja tulot/menot ovat annettu pylväsdiagrammin muodossa sekä kategoriat joihin rahaa on kulunut kuukauden aikana. Jos haetulta ajalta ei löydy lisättyjä tietoja, käyttäjälle annetaan ilmoitus uudessa näkymässä.

## Sovelluksen toiminnallisuus
### Sisäänkirjautuminen
- Käyttäjä luo järjestelmään käyttäjätunnuksen
	- käyttäjätunnus pitää olla vähintään 4 merkkiä pitkä ja maksimissaan 12 merkkiä
	- rekisteröitäessä uutta käyttäjätunnusta tarkistetaan ettei järjestelmässä ole jo vastaavaa käyttäjää eli jokainen käyttäjätunnus pitää olla erilainen
- Käyttäjän kirjautuminen sovellukseen
	- mikäli käyttäjällä on jo olemassa oleva käyttäjätunnus, kirjautuminen onnistuu syöttämällä tämä kirjautumisnäkymässä
	- jos käyttäjää ei löydy järjestelmästä, tästä tulee ilmoitus näytölle

### Onnistuneen sisäänkirjautumisen jälkeen
- Käyttäjälle aukeaa näkymä, jossa on listattuna Tulot, Menot, Tilastot ja Kirjaudu ulos -kohdat. Näistä valitsemalla "save income" tai "save expense" käyttäjä pääsee tallentamaan haluamansa tiedot, mutta sitä ennen käyttäjälle aukeaa uusi näkymä, jossa käyttäjän tulee vielä varmentaa antamansa tiedot.
	- Tuloille ja menoille on omat kategoriavalikkonsa, josta käyttäjä saa valita itselleen sopivan tyypin. Tämän jälkeen kategoriavalikot yhdistyvät ja näihin tulee asettaa summa, kuukausi ja vuosi. Kaikki kohdat ovat täytettävä ennen tallennusta, muutoin sovellus ei päästä käyttäjää eteenpäin.
	- Kategoriat on ennalta annettu käyttäjälle. Käyttäjä ei pysty näihin itse kirjoittamaan, ainoastaan summa-kohtaan käyttäjä pystyy syöttämään numeroita.
	- Tilastot menoista ja tuloista aukeavat uuteen ikkunaan, käyttäjä näkee täältä valitsemansa kuukauden ja vuoden kulutuksensa pylväsdiagrammin muodossa. Tässä näkyy menojen ja tulojen kategoriat sekä summa paljonko tiettyyn kategoriaan on mennyt rahaa. 
	- Kirjaudu ulos-nappula, käyttäjä kirjautuu ulos järjestelmästä.
	- Käyttäjän tekemät tulo/meno-tallennukset tallennetaan vasta, kun käyttäjä on varmistanut valintansa uudessa näkymässä.
	- Päänäkymässä tulisi näkyä suunnilleen n. 5 viimeisintä lisäystä tuloihin ja/tai menoihin. Käyttäjän lisätessä uuden menon/tulon, tulee vielä painaa refresh-nappulaa, jolloin päivitys tulee myös päänäkymään näkyviin.

### Jatkokehitysideat
- Sovellusta voisi jatkossa kehittää muun muassa seuraavasti:
	- Tilastoja voisi tarkastella vuositasolla.
	- Päivämäärät esim. lisätessä menoja.
	- Päänäkymästä pystyisi siirtymään osioon, jossa näkyisi kaikki asetetut tulot ja menot aikajärjestyksessä.
	- Käyttäjä saisi itse lisätä kategoriavalikkoon muutaman vaihtoehdon.
	- Käyttäjä tarvitsisi sisäänkirjautuessa myös salasanan.
