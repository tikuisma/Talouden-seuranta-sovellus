# Vaatimusmäärittely
_____________________

## Sovelluksen käyttötarkoitus
Sovelluksella käyttäjät pystyvät pitämään kirjaa tuloista ja menoista eli tarkoituksena on pitää kirjaa käyttäjän taloudesta. Sovellusta on mahdollista käyttää useampi käyttäjä, mutta jokaisella on oma käyttäjätunnus. 


## Käyttäjät
Sovelluksen käyttäjänä olisi tarkoitus toimia vain yksi käyttäjärooli eli ns. normaali käyttäjä. 


## Käyttöliittymäluonnos
Sovellus koostuu kolmesta eri näkymästä, suuntaa antava luonnos ohessa:
![Vaatimusmäärittelyluonnos](https://user-images.githubusercontent.com/93583969/145101911-834817d1-7e65-4f0c-b586-16e6c601be02.jpg)
Sovelluksen käynnistäessä olisi ensin tarkoitus tulla käyttäjän kirjautumisnäkymä, jonka jälkeen jo rekisteröitynyt käyttäjä laittaa käyttäjätunnuksensa ja kirjautuu sisään tai rekisteröimätön käyttäjä ensin rekisteröityy ja sitten kirjautuu sisään juuri luomallaan tunnuksella. Tässä näkymässä pystyy siis luomaan sekä käyttäjän että jo luotu käyttäjä pystyy sisäänkirjautumaan. Kirjautumisen jälkeen käyttäjälle avautuu näkymä, jossa käyttäjä voi lisätä itselleen menon ja/tai tulon. Kun käyttäjä haluaa tallentaa tulon/menon, ilmestyy näkyviin vielä uusi näkymä, jossa käyttäjältä varmistetaan vielä haluttu tallennus. Tällä yritetään minimoida käyttäjän tekemät vahinkopainallukset sekä se antaa käyttäjälle vielä mahdollisuuden tarkistaa tiedot, joita ollaan tallentamassa. Tuloihin ja menoihin käyttäjä saa ennen tallentamista valita vetolaatikoista itselleen sopivan kategorian ja lisätä kuukauden sekä vuoden ja laittaa summan. Kaikki kohdat tulee täyttää, muutoin sovellus ei anna käyttäjän tallentaa tietoja. Tilastoista nähdään kuukausittaiset menot sekä kategoriat joihin rahaa on kulunut kuukauden aikana.


## Sovelluksen toiminnallisuus
### Sisäänkirjautuminen 
- **Tämä osio on valmis**
- Käyttäjä luo järjestelmään käyttäjätunnuksen
	- käyttäjätunnus pitää olla vähintään 4 merkkiä pitkä ja maksimissaan 12 merkkiä
	- rekisteröitäessä uutta käyttäjätunnusta tarkistetaan ettei järjestelmässä ole jo vastaavaa käyttäjää eli jokainen käyttäjätunnus pitää olla erilainen
- Käyttäjän kirjautuminen sovellukseen
	- mikäli käyttäjällä on jo olemassa oleva käyttäjätunnus, kirjautuminen onnistuu syöttämällä tämä kirjautumisnäkymässä
	- jos käyttäjää ei löydy järjestelmästä, tästä tulee ilmoitus näytölle

### Onnistuneen sisäänkirjautumisen jälkeen
- Käyttäjälle aukeaa näkymä, jossa on listattuna Tulot, Menot, Tilastot ja Kirjaudu ulos -kohdat. Näistä valitsemalla "save income" tai "save expense" käyttäjä pääsee tallentamaan haluamansa tiedot, mutta sitä ennen käyttäjälle aukeaa uusi näkymä, jossa käyttäjän tulee vielä varmentaa antamansa tiedot.
	- **Tehty:** Tuloille ja menoille on omat kategoriavalikkonsa, josta käyttäjä saa valita itselleen sopivan tyypin. Tämän jälkeen kategoriavalikot yhdistyvät ja näihin tulee asettaa summa, kuukausi ja vuosi. Kaikki kohdat ovat täytettävä ennen tallennusta, muutoin sovellus ei päästä käyttäjää eteenpäin.
	- **Tehty:** Kategoriat on ennalta annettu käyttäjälle. Käyttäjä ei pysty näihin itse kirjoittamaan, ainoastaan summa-kohtaan käyttäjä pystyy syöttämään numeroita.
	- **Tehty:** Tilastot menoista aukeavat uuteen ikkunaan, käyttäjä näkee täältä valitsemansa kuukauden ja vuoden kulutuksensa pylväsdiagrammin muodossa. Tässä näkyy menojen kategoriat ja summa paljonko tiettyyn kategoriaan on mennyt rahaa. 
	- **Vielä tekemättä:** Kirjaudu ulos-nappula, käyttäjä kirjautuu ulos järjestelmästä.
	- **Tehty:** Käyttäjän tekemät tulo/meno-tallennukset tallennetaan vasta, kun käyttäjä on varmistanut valintansa uudessa näkymässä.
	- **Vielä tekemättä:** Päänäkymässä tulisi näkyä suunnilleen n. 5 viimeisintä lisäystä tuloihin/menoihin ja kuukauden vaihtuessa, nämä tyhjentyvät. 

### Jatkokehitysideat
- Ajan salliessa sovellusta voisi kehittää muun muassa seuraavasti:
	- Tilastoja voisi tarkastella vuositasolla.
	- Päivämäärät esim. lisätessä menoja.
	- Päänäkymästä pystyisi siirtymään osioon, jossa näkyisi kaikki asetetut tulot ja menot aikajärjestyksessä.
	- Käyttäjä saisi itse lisätä kategoriavalikkoon muutaman vaihtoehdon.
	- Käyttäjä tarvitsisi sisäänkirjautuessa myös salasanan.
