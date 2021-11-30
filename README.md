# Talouden seuranta -sovellus

Tarkoituksena tehdä sovellus, jossa käyttäjä pystyy sekä lisäilemään menoja että tuloja eli seurata omaa taloudellista tilannetta. Sovellusta voi käyttää useampi käyttäjätunnuksen luonut henkilö. Käyttäjätunnukselle tallentuu kaikki käyttäjän tekemät lisäykset.

Oman sovelluksen teko on osa Helsingin yliopiston Tietojenkäsittelytieteen Ohjelmistotekniikka-kurssia.

## Dokumentaatio
- [Tuntikirjanpito](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](https://github.com/tikuisma/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

## Asennus

1. Asenna riippuvuudet komennolla: ```poetry install```

2. Käynnistä virtuaaliympäristö komennolla: ```poetry shell```

3. Käynnistä sovellus komennolla: ```poetry run invoke start```


## Komentorivitoiminnot
### Ohjelman suorittaminen

- Ohjelman pystyy suorittamaan komennolla: ```poetry run invoke start```

### Ohjelman testaus

- Testit suoritetaan komennolla: ```poetry run invoke test```

### Testikattavuus

- Testikattavuusraportin voi generoida **src-hakemiston sisällä** komennolla: **poetry run invoke coverage-report**
- Raportin tekeminen ei onnistu ot-harjoitustyo -hakemiston alla
- Raportti generoituu htmlcov-hakemistoon.
