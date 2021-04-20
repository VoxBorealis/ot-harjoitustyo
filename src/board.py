import os
import random
import pygame
from card import Card


class Board:
    def __init__(self, ROWS, COLUMNS, CARD_LEN, CARD_SPACE):
        self.rows = ROWS
        self.columns = COLUMNS
        current_path = os.path.dirname(__file__)
        resource_path = os.path.join(current_path, 'assets')

        self.background_surface = pygame.image.load(
            os.path.join(resource_path, 'Background.png')).convert()
        self.card_backside = pygame.image.load(
            os.path.join(resource_path, 'BACKSIDE.png')).convert()

        # Luo cards taulukon, johon se lisää Card pareja 9kpl.
        # Card sisältää Surface-olion, id:n,
        self.cards = []
        current_path = os.path.dirname(__file__)
        resource_path = os.path.join(current_path, 'assets')
        directory = os.path.join(resource_path, 'cards')

        k = 0
        for filename in os.listdir(directory):
            file = os.path.join(directory, filename)
            if os.path.isfile(file):
                self.card = pygame.image.load(file)
                for j in range(2):
                    self.cards.append(Card(self.card, k))
                k += 1
        random.shuffle(self.cards)

        # Luo 3x6 Ruudukon.
        # Siis tyhjiä kortin kokoisia Rect-olioita
        # Nyt samalla antaa cards olioille locationin (rectin)
        self.card_grid = [[] for i in range(self.rows)]
        k = 0
        for i in range(self.rows):
            if i == 0:
                for j in range(self.columns):
                    if j == 0:
                        self.card_grid[i].append(
                            pygame.Rect((CARD_SPACE), (CARD_LEN)))
                        self.cards[k].set_location(self.card_grid[i][j])
                    else:
                        self.card_grid[i].append(pygame.Rect(
                            self.card_grid[i][j-1].x + CARD_LEN[0] + CARD_SPACE[0],
                            CARD_SPACE[1], CARD_LEN[0], CARD_LEN[1]))
                        self.cards[k].set_location(self.card_grid[i][j])

                    k += 1
            else:
                for j in range(self.columns):
                    if j == 0:
                        self.card_grid[i].append(pygame.Rect(
                            CARD_SPACE[0], self.card_grid[i-1][j].y + CARD_LEN[1] + CARD_SPACE[1],
                            CARD_LEN[0], CARD_LEN[1]))
                        self.cards[k].set_location(self.card_grid[i][j])

                    else:
                        self.card_grid[i].append(pygame.Rect(
                            self.card_grid[i][j-1].x + CARD_LEN[0] + CARD_SPACE[0],
                            self.card_grid[i-1][j].y + CARD_LEN[1] + CARD_SPACE[1],
                            CARD_LEN[0], CARD_LEN[1]))
                        self.cards[k].set_location(self.card_grid[i][j])

                    k += 1
