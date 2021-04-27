import random
import pygame
from card import Card
from file_loader import FileLoader


class Board:
    def __init__(self, ROWS, COLUMNS, CARD_LEN, CARD_SPACE):
        self.rows = ROWS
        self.columns = COLUMNS
        self.file_loader = FileLoader()

        self.background_surface = self.file_loader.get_background()
        self.card_backside = self.file_loader.get_backside()
        self.stat_grid = self.file_loader.get_stat_grid()

        # Luo cards taulukon, johon se lisää Card pareja 9kpl.
        # Card sisältää Surface-olion(png), id:n,
        self.cards = []
        id_ = 0
        for card in self.file_loader.get_cards():
            for j in range(2):
                self.cards.append(Card(card, id_))
            id_ += 1
        random.shuffle(self.cards)

        # Luo 3x6 Ruudukon.
        # Siis tyhjiä kortin kokoisia Rect-olioita
        # Nyt samalla antaa cards olioille locationin (rectin)
        # Muuttuja k muistaa monesko kortti on käsittelyssä.
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
