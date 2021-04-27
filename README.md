# Ohjelmistotekniikka, harjoitustyö

# Python Muistipeli

Sovellus on perinteinen muistipeli, joka on rakennettu pygame-kirjastolla.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/VoxBorealis/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/VoxBorealis/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

Arkkitehtuurin(kaavioiden) tekeminen on osoittautunut hankalaksi, joten se on vielä kesken.

## Asennus

1. Asenna riippuuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä peli komennolla:

```bash
poetry run invoke start
```

### Testaus

Pygamen testauskin on osoittautunut vaikeaksi, niin tämäkin on vielä vaiheessa.

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Pylint

Pylint testin voi suorittaa komennolla:

```bash
poetry run invoke lint
```
