# Testausdokumentti
Ohjelmaa on testattu automatisoiduilla unittest -testiohjelmalla. 

## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka
Käyttöliittymästä on kutsuja funktioille, luokille ja näiden metodeille. Luokkiin on alustettu omat tietokannat tallennukselle. Tätä varten testissä on käytössä ``TestUserDatabase`` ja ``TestDatabase``.

### Repositorio-luokat
Repositorio-luokkia ``UserDatabase`` ja ``Database`` testataan ainoastaan testien käyttöön tehdyillä tiedostoilla. Tiedostojen nimet on konfiguroitu .env.test-tiedostoon. Molempia luokkia testataan ``TestUserDatabase``- ja ``TestDatabase`` -luokilla.

### Testauskattavuus
Käyttöliittymää lukuunottamatta sovelluksen testauksen haarautumakattavuus on vaihtelevaa, 28-100%.

## Järjestelmätestaus
Sovelluksen järjestelmätestaus on toteutettu manuaalisesti.

### Asennus ja konfigurointi
Sovellus on haettu ja sitä on testattu käyttöohjeen kuvaamalla tavalla vain Linux-ympäristössä.
Sovellusta on testattu ns. alkutilanteesta lähtien, jossa käyttäjiä ja näiden lisäilemiä tuloja/menoja ei vielä ole, jolloin ohjelma on luonut näille tietokannan että tilanteissa, joissa käyttäjät ja tallennetut tiedot ovat olleet jo olemassa.

### Toiminnallisuudet
Toiminnallisuuksia on pystytty testaamaan ainoastaan käyttäjän luonnin/sisäänkirjautumisen osalta. Muut osat ovat ohjelman koodissa ns. lukittu käyttäjältä tai nämä ilmoittavat käyttäjälle virheilmoituksen graafisessa käyttöliittymässä.

## Sovellukseen jääneet laatuongelmat
Sovellus ei anna tällä hetkellä järkeviä virheilmoituksia.
Laatuongelmia ovat mm.:
- SQLiten tietokantaa ei ole alustettu eli sitä ei pysty millään komennolla suorittamaan.

Testien tekeminen oli ylipäätään hieman hankalaa. Ohjelman koodi olisi pitänyt alusta alkaen rakentaa aivan toisella tavalla, jotta olisin päässyt enemmän testailemaan. Tällä hetkellä testaaminen on hankalaa ja suppeaa, koska kaikki pyörii Tkinterin eli graafisen käyttöliittymän ympärillä. Testejä olen pyrkinyt tekemään niin kattavasti kuin ohjelman koodini sen sallii. Kurssin viimeisillä viikoilla en uskaltanut enää lähteä muuttamaan koko projektin koodia toisenlaiseksikaan, mutta tekisin eri tavalla, jos aloittaisin nyt alusta.
