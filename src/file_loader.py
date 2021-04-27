import os
import pygame

class FileLoader:
    def __init__(self):
        self._current_path = os.path.dirname(__file__)
        self._resource_path = os.path.join(self._current_path, 'assets')

    def get_background(self):
        return pygame.image.load(os.path.join(self._resource_path, 'Background.png')).convert()

    def get_backside(self):
        return pygame.image.load(os.path.join(self._resource_path, 'BACKSIDE.png')).convert()

    def get_cards(self):
        directory = os.path.join(self._resource_path, 'cards')
        cards = []
        for filename in os.listdir(directory):
            file = os.path.join(directory, filename)
            if os.path.isfile(file):
                cards.append(pygame.image.load(file).convert())
        return cards
    def get_stat_grid(self):
        return pygame.image.load(os.path.join(self._resource_path, 'STATGRID.png')).convert()

    def get_game_over_screen(self):
        return pygame.image.load(os.path.join(self._resource_path, 'GAMEOVER.png')).convert()
