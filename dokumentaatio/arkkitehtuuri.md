# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattaa kerrosarkkitehtuuria ja pakkausrakenne on seuraava:

![Pakkauskaavio] (./kuvat/Pakkauskaavio.jpg)

Pakkaus ui sisältää käyttöliittymästä huolehtivan koodin, src sisältää pelin logiikan ja ylläpidon.


## Käyttöliittymä

Pelissä on vain kaksi eri näkymää.
- Peli on käynnissä ja kortit ovat ruudulla
- Peli on pelattu loppuun, jolloin game-over näkymä on ruudulla.

## Sovelluslogiikka

![Luokkakaavio] (./kuvat/Luokkakaavio.jpg)


Pelin ylläpidosta huolehtii GameLoop-luokka ja se on riippuvainen kaikista muista luokista. Board-luokka vastaa peliruudukon luomisesta ja korttien tilan ylläpidosta. Card-luokka vastaa yksittäisen kortin luonnista ja ylläpidosta. Renderer-luokka vastaa eri elementtien piirtämisestä ruudulle. FileLoader-luokka huolehtii tieodstojen lataamisesta. EventQueue-luokka on vastuussa tapahtumienkäsittelystä, kuten pelaajan syötteiden käsittely. Clock-luokka huolehtii pelin ajoituksista.

## Tiedon pysyväistallennus

GameLoop-luokassa on koodia, joka tallettaa pelaajan tilastoja scores.txt tiedostoon, pelaajan voittaessa pelin.
