# Testausdokumentti
Ohjelmaa on testattu automatisoiduilla unittest -testiohjelmalla. Käyttöliittymän testaus on suoritettu manuaalisesti.

## Yksikkö- ja integraatiotestaus
### Sovelluslogiikka
Käyttöliittymästä on kutsuja funktioille, luokille ja näiden metodeille. Luokilla hallitaan SQLite-tietokantaan tallennusta. Sisäänkirjautumisesta vastaa *Log_in*-moduuli. Tietokantahakuja suorittaa *database*-moduuli. Tätä varten testeissä on käytössä ``TestUserDatabase``, joka testaa käyttäjän luomista ja sisäänkirjautumista sekä ``TestDatabase``, joka testaa käyttäjän tekemiä tallennuksia tietokantaan.

### Repositorio-luokat
Repositorio-luokkia ``UserDatabase`` ja ``Database`` testataan ainoastaan testien käyttöön tehdyillä tietokannoilla. Tietokantojen nimet on konfiguroitu .env.test-tiedostoon. Molempia luokkia testataan ``TestUserDatabase`` ja ``TestDatabase`` nimisillä luokilla.

### Testauskattavuus
Käyttöliittymää lukuunottamatta sovelluksen testauksen haarautumakattavuus on vaihtelevaa.

![Screenshot from 2021-12-23 18-44-18](https://user-images.githubusercontent.com/93583969/147269559-c10fdd18-558c-4d52-9cf3-1fbcdd9ea0d2.png)

## Järjestelmätestaus
Sovelluksen järjestelmätestaus on toteutettu manuaalisesti.

### Asennus ja konfigurointi
Sovellus on haettu ja sitä on testattu käyttöohjeen kuvaamalla tavalla vain Linux-ympäristössä.
Sovellusta on testattu ns. alkutilanteesta lähtien, jossa käyttäjiä ja näiden lisäilemiä tuloja/menoja ei vielä ole, jolloin ohjelma on luonut näille tietokannan että tilanteissa, joissa käyttäjät ja tallennetut tiedot ovat olleet jo olemassa.

### Toiminnallisuudet
Toiminnallisuuksia on testattu käyttäjän luonnin/sisäänkirjautumisen osalta unittestilla. Muut ohjelman osat, kuten graafien ja taulukoiden generoituminen oikein on testattu käsin. Suurin osa ohjelmalle annettavista syötteistä on lukittu käyttöliittymään, joten käyttäjän vapaasti muokattavia kenttiä on hyvin rajallisesti ja nämä ilmoittavat tarvittaessa käyttäjälle virheilmoituksen graafisessa käyttöliittymässä.

## Sovellukseen jääneet laatuongelmat

Testien tekeminen oli ylipäätään hieman hankalaa. Ohjelman koodi olisi pitänyt alusta alkaen rakentaa aivan toisella tavalla, jotta olisin päässyt enemmän testailemaan. Tällä hetkellä testaaminen on hankalaa ja suppeaa, koska kaikki pyörii Tkinterin eli graafisen käyttöliittymän ympärillä. Testejä olen pyrkinyt tekemään niin kattavasti kuin ohjelman koodini sen sallii. Kurssin viimeisillä viikoilla en uskaltanut enää lähteä muuttamaan koko projektin koodia toisenlaiseksi, mutta rakentaisin koodin eri tavalla, jos aloittaisin nyt alusta.

Parannettavaa esimerkiksi:
- Käyttöliittymän ja sovelluksen backendin erottaminen selkeämmin
- Testien kattavuuden parantaminen, käyttöliittymän puolen testausta voisi automatisoida
