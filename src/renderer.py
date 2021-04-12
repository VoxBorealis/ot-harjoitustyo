import pygame

class Renderer:
    def __init__(self, display, board):
        self._display = display
        self._board = board
        
    def render(self):
        self._display.blit(self._board.background_surface, (0,0))
        for i in range(self._board.ROWS):
            for j in range(self._board.COLUMNS):
                self._display.blit(self._board.CARD, self._board.CARD_GRID[i][j])
        
        pygame.display.update()

    def render_cards(self):
        for i in range(3):
            for j in range(6):
                self._display.blit()