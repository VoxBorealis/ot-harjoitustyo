import unittest
import pygame
from board import Board
from ui.file_loader import FileLoader


class testBoard(unittest.TestCase):
    def setUp(self):
        self.display = pygame.display.set_mode((1280,820))
        self.file_loader = FileLoader()
        self.board = Board(3,6,(150,200),(54,30))
        pygame.init()
    
    def test_konstruktori_asettaa_arvot_oikein(self):
        self.assertEqual(self.board.rows, 3)
        self.assertEqual(self.board.columns, 6)

    def test_file_loader(self):
        self.assertIsNotNone(self.board.background_surface)
        self.assertIsNotNone(self.board.card_backside)
        self.assertIsNotNone(self.board.stat_grid)
    
    def test_cards_array(self):
        self.assertEqual(3*6, len(self.board.cards))

    def test_card_grid(self):
        self.assertEqual(str(self.board.card_grid[2][2]), "<rect(462, 490, 150, 200)>")
