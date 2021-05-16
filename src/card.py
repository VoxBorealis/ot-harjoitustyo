

class Card:
    """Luokka, joka kuvaa yksittäistä korttia.

    Attributes:
        surface: Pygame.Surface olio, joka sisältää png formaatissa olevan kuvan
        id_: Kokonaislukuarvo, näistä muodostuvat kortti parit.
            Eli kahdella kortilla on aina sama id_
        turned_over: Boolean-arvo, joka kuvastaa, onko kortti käännetty kuvapuoli ylöspäin
        matched: Boolean-arvo, joka kuvastaa, onko kortille löydetty jo pari
        location: Aluksi tyhjä, mutta tähän laitetaan Pygame.Rect olio,
                jota käytetään antamaan kortille sijainti
    """

    def __init__(self, surface, id_):
        """Luokan konstruktori. Luo uuden kortin.

        Args:
            surface (Pygame.Surface): Sisältää png formaatissa olevan kuvan
            id_ (Kokonaislukuarvo): kuvaa kortin id:tä
        """

        self.surface = surface
        self.id_ = id_
        self.turned_over = False
        self.matched = False
        self.location = None

    def get_surface(self):
        """Palauttaa kortin surface:n, eli Pygame.Surface olion, joka sisältää
            png-formaatissa olevan kuvan

        Returns:
            pygame.Surface: png-formaatissa oleva kuva.
        """
        return self.surface

    def get_id(self):
        """Palauttaa kortin id:n

        Returns:
            int: id
        """
        return self.id_

    def set_location(self, location):
        """Asettaa kortille sijainnin eli pygame.Rect olion.

        Args:
            location (pygame.Rect): Kortin sijainti ruudukolla.
        """
        self.location = location

    def get_location(self):
        """Palauttaa kortin sijainnin, eli pygame.Rect:in

        Returns:
            pygame.Rect: Kortin sijainti
        """
        return self.location

    def turn_over(self):
        """Kääntää kortin ylösalaisin
        """
        if self.turned_over is False:
            self.turned_over = True
        else:
            self.turned_over = False

    def get_turned_over(self):
        """Palauttaa kortin turned_over tilan, joka kertoo onko kortti käännetty.

        Returns:
            Boolean: Kertoo onko kortti käännetty. False, jos kortin takapuoli on esillä.
            True, jos kortin kuvapuoli on esillä.
        """
        return self.turned_over

    def set_match(self):
        """Merkitsee kyseisen kortin paritetuksi, jolloin tiedetään mitkä kortit ovat löydetty.
        """
        self.matched = True

    def get_matched(self):
        """Palauttaa muuttujan matched tilan, joka kertoo onko kortille löydetty jo pari.

        Returns:
            Boolean: Kertoo onko kortille löydetty jo pari.
        """
        return self.matched
