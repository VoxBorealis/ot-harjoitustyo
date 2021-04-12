import pygame
import os



class Board:
    def __init__(self, ROWS, COLUMNS, CARD_LEN, CARD_SPACE):
        self.ROWS = ROWS
        self.COLUMNS = COLUMNS
        current_path = os.path.dirname(__file__)
        resource_path= os.path.join(current_path, 'assets')

        self.background_surface = pygame.image.load(os.path.join(resource_path, 'Background.png')).convert()

        cards = []
        for i in range(9):
            current_path = os.path.dirname(__file__)
            resource_path= os.path.join(current_path, 'assets')

            self.CARD = pygame.image.load(os.path.join(resource_path, 'BACKSIDE.png')).convert()
            for j in range(2):
                cards.append(self.CARD.get_rect())


        self.CARD_GRID = [[] for i in range(ROWS)]
        k = 0
        for i in range(ROWS):
            if i == 0:
                for j in range(COLUMNS):
                    if j == 0:
                        cards[k].move_ip((CARD_SPACE))
                        self.CARD_GRID[i].append(cards[k])
                    else:
                        cards[k].move_ip(self.CARD_GRID[i][j-1].x + CARD_LEN[0] + CARD_SPACE[0], CARD_SPACE[1])
                        self.CARD_GRID[i].append(cards[k])
                    k+=1
            else:
                for j in range(COLUMNS):
                    #print(k, i, j)
                    #print(CARD_GRID)
                    if j == 0:
                        cards[k].move_ip(CARD_SPACE[0], self.CARD_GRID[i-1][j].y + CARD_LEN[1] + CARD_SPACE[1])
                        self.CARD_GRID[i].append(cards[k])
                    else:
                        cards[k].move_ip(self.CARD_GRID[i][j-1].x + CARD_LEN[0] + CARD_SPACE[0], self.CARD_GRID[i-1][j].y + CARD_LEN[1] + CARD_SPACE[1])
                        self.CARD_GRID[i].append(cards[k])
                    k+=1