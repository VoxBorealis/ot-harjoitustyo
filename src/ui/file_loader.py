import os
from pathlib import Path
import pygame

class FileLoader:
    """Luokka, joka antaa metodeja kuvien hakuun tiedostoista

    Attributes:
        _current_path: Merkkijonoarvo, joka kertoo nykyisen osoitteen
        _resource_path: Merkkijonoarvo, joka kertoo assets kansion osoitteen
    """

    def __init__(self):
        """Luokan konstruktori, luo uuden FileLoader olion
        """
        self._current_path = os.path.dirname(__file__)
        self._resource_path = os.path.join(str(Path(self._current_path).parents[0]), 'assets')

    def get_background(self):
        """Hakee Background.png

        Returns:
            pygame.Surface: Palauttaa Background.png:n Surface muodossa
        """
        return pygame.image.load(os.path.join(self._resource_path, 'Background.png')).convert()

    def get_backside(self):
        """Hakee Backside.png kuvan tiedostoista

        Returns:
            pugame.Surface: Palauttaa BACKSIDE.png:n Surface muodossa
        """
        return pygame.image.load(os.path.join(self._resource_path, 'BACKSIDE.png')).convert()

    def get_cards(self):
        """Hakee kaikkien korttien kuvat

        Returns:
            []: Palauttaa taulukon, joka sisältää kaikkien korttien kuvat pygame.Surface muodossa
        """
        directory = os.path.join(self._resource_path, 'cards')
        cards = []
        for filename in os.listdir(directory):
            file = os.path.join(directory, filename)
            if os.path.isfile(file):
                cards.append(pygame.image.load(file).convert())
        return cards
    def get_stat_grid(self):
        """Hakee STATGRID.png

        Returns:
            pygame.Surface: Palauttaa STATGRID.png:n pygame.Surface muodossa
        """
        return pygame.image.load(os.path.join(self._resource_path, 'STATGRID.png')).convert()

    def get_game_over_screen(self):
        """Hakee GAMEOVER.png

        Returns:
            pygame.Surface: Palauttaa GAMEOVER.png:n pygame.Surface muodossa
        """
        return pygame.image.load(os.path.join(self._resource_path, 'GAMEOVER.png')).convert()
