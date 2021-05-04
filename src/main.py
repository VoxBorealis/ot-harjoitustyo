import pygame
from game_loop import GameLoop
from entities.event_queue import EventQueue
from entities.clock import Clock
from ui.renderer import Renderer
from board import Board

WIDTH = 1280
HEIGHT = 820

ROWS = 3
COLUMNS = 6
CARD_LEN = (150, 200)
CARD_SPACE = (54, 30)


def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Memory Game")

    board = Board(ROWS, COLUMNS, CARD_LEN, CARD_SPACE)
    event_queue = EventQueue()
    renderer = Renderer(display, board)
    clock = Clock()
    game_loop = GameLoop(renderer, event_queue, clock, board)

    pygame.init()

    game_loop.start()


if __name__ == "__main__":
    main()
