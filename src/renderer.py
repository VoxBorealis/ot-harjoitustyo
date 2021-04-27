import pygame

from file_loader import FileLoader

class Renderer:
    def __init__(self, display, board):
        self._display = display
        self._board = board
        self._file_loader = FileLoader()

    def render(self, turns):
        self._display.blit(self._board.background_surface, (0, 0))
        self._display.blit(self._board.stat_grid, (0, 720))

        for card in self._board.cards:
            if card.get_turned_over():
                self._display.blit(card.get_surface(), card.get_location())
            else:
                self._display.blit(self._board.card_backside,
                                   card.get_location())
        font = pygame.font.SysFont(None, 30)
        img = font.render('Turns: ' + str(turns), True, (255, 255, 255))
        self._display.blit(img, (20, 770))

        pygame.display.update()

    def render_go_screen(self, turns, mistakes, time):
        self._display.blit(self._file_loader.get_game_over_screen(), (250, 150))

        font = pygame.font.SysFont(None, 45)
        draw_turns = font.render('Turns: ' + str(turns), True, (255, 255, 255))
        self._display.blit(draw_turns, (400, 200))

        draw_mistakes = font.render('Mistakes: ' + str(mistakes), True, (255, 255, 255))
        self._display.blit(draw_mistakes, (400, 300))

        draw_time = font.render('Time: ' + time, True, (255, 255, 255))
        self._display.blit(draw_time, (400, 400))

        message = font.render('WORK IN PROGRESS...', True, (255, 255, 255))
        self._display.blit(message, (400, 500))

        pygame.display.flip()
        