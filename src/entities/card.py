

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
        return self.surface

    def get_id(self):
        return self.id_

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def turn_over(self):
        if self.turned_over is False:
            self.turned_over = True
        else:
            self.turned_over = False

    def get_turned_over(self):
        return self.turned_over

    def set_match(self):
        self.matched = True

    def get_matched(self):
        return self.matched
