# Talouden seuranta -sovellus

Tarkoituksena tehdä sovellus, jossa käyttäjä pystyy sekä lisäilemään menoja että tuloja eli seurata omaa taloudellista tilannetta. Sovellusta voi käyttää useampi käyttäjätunnuksen luonut henkilö. Käyttäjätunnukselle tallentuu kaikki käyttäjän tekemät lisäykset.

Oman sovelluksen teko on osa Helsingin yliopiston Tietojenkäsittelytieteen Ohjelmistotekniikka-kurssia.

## Dokumentaatio
- [Tuntikirjanpito](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

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
	2. komento: ```pylint src```
- Koodin laadun tämänhetkinen pisteytys on 8.7/10 

### Ohjelman testaus:

- Testit suoritetaan komennolla: ```poetry run invoke test```

### Testikattavuus

- Testikattavuusraportin voi generoida komennolla: ```poetry run invoke coverage-report```
- Raportti generoituu htmlcov-hakemistoon.

### Release

[Release](https://github.com/tikuisma/ot-harjoitustyo/releases/tag/viikko5)
