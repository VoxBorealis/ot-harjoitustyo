import unittest
import pygame
from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(pygame.Surface((100,100)), 1)
    
    def test_konstruktori_asettaa_id_oikein(self):
        self.assertEqual(self.card.id, 1)

    def test_get_surface_toimii_oikein(self):
        self.assertEqual(self.card.surface, self.card.get_surface())

    def test_get_id_toimii_oikein(self):
        self.assertEqual(self.card.get_id(), 1)

    

