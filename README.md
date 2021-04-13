# Ohjelmistotekniikka, harjoitustyö

# Python Muistipeli

Sovellus on perinteinen muistipeli, joka on rakennettu pygame-kirjastolla.

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/VoxBorealis/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/VoxBorealis/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alkutoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä peli komennolla:

```bash
poetry run invoke start
```

### Testaus

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
