import unittest
import pygame

from board import Board
from game_loop import GameLoop

class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0

class StubEvent:
    def __init__(self, event_type):
        self.type = event_type

class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        pass

class StubRenderer:
    def render(self):
        pass


WIDTH = 1280
HEIGHT = 820
ROWS = 3
COLUMNS = 6
CARD_LEN = (150, 200)
CARD_SPACE = (54, 30)



#class TestGameLoop(unittest.TestCase):
#    def setUp(self):
#        self.board = Board(ROWS, COLUMNS, CARD_LEN, CARD_SPACE)
#        
#
#    def test_something(self):
#        events = [
#            StubEvent(pygame.MOUSEBUTTONDOWN),
#        ]
#
#        game_loop = GameLoop(
#            StubRenderer(),
#            StubEventQueue,
#            StubClock,
#            self.board
#        )
#
#        game_loop.start()
#
#
#        self.assertEqual(game_loop._turned, 0)
        