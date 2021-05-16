import unittest
import pygame

from board import Board
from game_loop import GameLoop
from event_queue import EventQueue
from card import Card

class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0

class StubEvent:
    def __init__(self, event_type, button, pos):
        self.type = event_type
        self.button = button
        self.pos = pos

class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events

class StubRenderer:
    def render(self):
        pass

    def render_board(self, turns, mistakes, time):
        pass

    def render_go_screen(self, turns, mistakes, time):
        pass


WIDTH = 1280
HEIGHT = 820
ROWS = 3
COLUMNS = 6
CARD_LEN = (150, 200)
CARD_SPACE = (54, 30)



class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.board = Board(ROWS, COLUMNS, CARD_LEN, CARD_SPACE)
        
        

    def test_quit_game_loop(self):
        events = [
            StubEvent(pygame.QUIT, 1, (1280,820))
        ]
        event_queue = StubEventQueue(events)

        game_loop = GameLoop(
            StubRenderer(),
            event_queue,
            StubClock(),
            self.board
        )
        game_loop.start()
        self.assertEqual(game_loop._handle_events(), False)

    def test_can_turn_card(self):
        events = [
            StubEvent(pygame.MOUSEBUTTONDOWN, 1, (100,100)), 
            StubEvent(pygame.QUIT, 1, (1280,820))
        ]
        event_queue = StubEventQueue(events)
        game_loop = GameLoop(
            StubRenderer(),
            event_queue,
            StubClock(),
            self.board
        )
        game_loop.start()

        self.assertEqual(len(game_loop._turned), 1)

    def test_can_get_match(self):
        events = [
            StubEvent(pygame.MOUSEBUTTONDOWN, 1, (0,0)), 
            StubEvent(pygame.QUIT, 1, (1280,820))
        ]
        event_queue = StubEventQueue(events)
        game_loop = GameLoop(
            StubRenderer(),
            event_queue,
            StubClock(),
            self.board
        )
        game_loop._turned.append(Card(pygame.Surface((100,100)), 1))
        game_loop._turned.append(Card(pygame.Surface((100,100)), 1))
        game_loop.start()
        

        self.assertEqual(len(game_loop._turned), 2)
        self.assertEqual(game_loop._turned[0].get_id(), 1)
        self.assertEqual(game_loop._turned[1].get_id(), 1)
    