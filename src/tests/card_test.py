import unittest
import pygame
from entities.card import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(pygame.Surface((100, 100)), 1)

    def test_konstruktori_asettaa_id_oikein(self):
        self.assertEqual(self.card.id_, 1)

    def test_get_surface_toimii_oikein(self):
        self.assertEqual(self.card.surface, self.card.get_surface())

    def test_get_id_toimii_oikein(self):
        self.assertEqual(self.card.get_id(), 1)
    
    def test_set_location_toimii(self):
        self.card.set_location(pygame.Rect(0,0,100,100))
        self.assertEqual(self.card.location, pygame.Rect(0,0,100,100))

    def test_get_location_toimii(self):
        self.assertEqual(self.card.get_location(), None)
    
    def test_turn_over_toimii_aluksi_false(self):
        self.card.turn_over()
        self.assertEqual(self.card.turned_over, True)
    
    def test_turn_over_toimii_aluksi_true(self):
        self.card.turn_over()
        self.card.turn_over()
        self.assertEqual(self.card.turned_over, False)

    def test_get_turned_over_toimii(self):
        self.assertEqual(self.card.turned_over, self.card.get_turned_over())

    def test_set_match_toimii(self):
        self.card.set_match()
        self.assertEqual(self.card.matched, True)

    def test_get_matched_toimii(self):
        self.assertEqual(self.card.matched, self.card.get_matched())
