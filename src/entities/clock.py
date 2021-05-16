import pygame


class Clock:
    """Luokka, joka huolehtii pelin ajoituksista. Käyttää pygamen clock muuttujaa.

    Attributes:
        _clock: pygamen Clock-olio
    """
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        self._clock.tick(fps)

    def get_ticks(self):
        return pygame.time.get_ticks()
