# Talouden seuranta -sovellus

Tarkoituksena tehdä sovellus, jossa käyttäjä pystyy sekä lisäämään menoja että tuloja eli seurata taloudellista tilannettaan. Sovellusta voi käyttää useampi käyttäjätunnuksen luonut henkilö. Käyttäjätunnukselle tallentuu kaikki käyttäjän tekemät lisäykset.

Oman sovelluksen teko on osa Helsingin yliopiston Tietojenkäsittelytieteen Ohjelmistotekniikka-kurssia.

## Dokumentaatio
- [Käyttöohje](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
- [Tuntikirjanpito](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuudet komennolla: ```poetry install```

2. Käynnistä virtuaaliympäristö komennolla: ```poetry shell```

3. Käynnistä sovellus komennolla: ```poetry run invoke start```


## Komentorivitoiminnot
### Ohjelman suorittaminen

- Ohjelman pystyy suorittamaan komennolla: ```poetry run invoke start```

### Koodin laadun tarkistaminen

- Koodin laadun pystyy tarkastamaan:
	1. ensin komento: ```poetry shell```
	2. komento: ```poetry run invoke lint```
- Koodin laadun pisteytys on 9.61/10. 

### Ohjelman testaus:

- Testit suoritetaan komennolla: ```poetry run invoke test```

### Testikattavuus

- Testikattavuusraportin voi generoida komennolla: ```poetry run invoke coverage-report```
- Raportti generoituu htmlcov-hakemistoon.

### Releaset

[Viikko 5 release](https://github.com/tikuisma/ot-harjoitustyo/releases/tag/viikko5)

[Viikko 6 release](https://github.com/tikuisma/ot-harjoitustyo/releases/tag/viikko6)

[Loppupalautuksen release](https://github.com/tikuisma/ot-harjoitustyo/releases/tag/Loppupalautus)
