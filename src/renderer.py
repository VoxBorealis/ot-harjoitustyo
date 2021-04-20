import pygame


class Renderer:
    def __init__(self, display, board):
        self._display = display
        self._board = board

    def render(self):
        self._display.blit(self._board.background_surface, (0, 0))

        for card in self._board.cards:
            if card.get_turned_over():
                self._display.blit(card.get_surface(), card.get_location())
            else:
                self._display.blit(self._board.card_backside,
                                   card.get_location())
        font = pygame.font.SysFont(None, 24)
        img = font.render('Turns: ', True, (255, 255, 255))
        self._display.blit(img, (20, 770))

        pygame.display.update()
