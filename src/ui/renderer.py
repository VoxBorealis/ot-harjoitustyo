import pygame

from ui.file_loader import FileLoader

class Renderer:
    """Luokka, jonka vastuulla on eri elementtien piirtäminen ruudulle

    Attributes:
        _display: pygame.Display-olio, joka on vastuussa peli-ikkunasta
        _board: Board-olio, joka on vastuussa peliruudukon luomisesta
        _file_loader: FileLoader-olio, joka on vastuussa kuvien hakemisesta assets kansiosta
    """
    def __init__(self, display, board):
        """Luokan konstruktori, joka luo uuden Renderer-olion

        Args:
            display (pygame.Display): pygame.Display-olio, joka on vastuussa peli-ikkunasta
            board (Board): Board-olio, joka on vastuussa peliruudukon luomisesta
        """
        self._display = display
        self._board = board
        self._file_loader = FileLoader()
        self.WHITE = (255, 255, 255)

    def render_board(self, turns, mistakes, time):
        """Piirtää peliruudukon eri elementit ruudulle

        Args:
            turns (int): Kokonaislukumuuttuja, joka kertoo kuinka monta vuoroa on pelattu
            mistakes (int): Kokonaislukumuuttuja,
                            joka kertoo kuinka monta virhettä pelaaja on tehnyt
            time (float): Float-muuttuja, joka kertoo kuinka kauan pelaaja on pelannut
        """
        self._display.blit(self._board.background_surface, (0, 0))
        self._display.blit(self._board.stat_grid, (0, 720))

        for card in self._board.cards:
            if card.get_turned_over():
                self._display.blit(card.get_surface(), card.get_location())
            else:
                self._display.blit(self._board.card_backside,
                                   card.get_location())
        font = pygame.font.SysFont(None, 30)
        img = font.render('Turns: ' + str(turns), True, (self.WHITE))
        self._display.blit(img, (20, 770))

        draw_mistakes = font.render('Mistakes: ' + str(mistakes), True, (self.WHITE))
        self._display.blit(draw_mistakes, (120, 770))

        draw_time = font.render('Elapsed Time: ' + str(time), True, (self.WHITE))
        self._display.blit(draw_time, (270, 770))

        pygame.display.update()

    def render_go_screen(self, turns, mistakes, time):
        """Piirtää pelin lopetusruudun

        Args:
            turns (int): Kokonaislukumuuttuja, joka kertoo montako vuoroa on pelattu
            mistakes (int): Kokonaislukumuuttuja, joka kertoo montako virhettä pelaaja on tehnyt
            time (float): Float-muuttuja, joka kertoo kuinka kauan peliä on pelattu
        """
        self._display.blit(self._file_loader.get_game_over_screen(), (250, 150))

        font = pygame.font.SysFont(None, 45)
        draw_turns = font.render('Turns: ' + str(turns), True, (self.WHITE))
        self._display.blit(draw_turns, (400, 200))

        draw_mistakes = font.render('Mistakes: ' + str(mistakes), True, (self.WHITE))
        self._display.blit(draw_mistakes, (400, 300))

        draw_time = font.render('Time: ' + str(time), True, (self.WHITE))
        self._display.blit(draw_time, (400, 400))

        message = font.render('ARTWORK IN PROGRESS...', True, (self.WHITE))
        self._display.blit(message, (400, 500))

        pygame.display.flip()
        