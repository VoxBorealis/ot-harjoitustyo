import unittest
import pygame

from clock import Clock

class testClock(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

    def test_get_ticks_toimii(self):
        self.clock.tick(30)
        self.assertEqual(self.clock.get_ticks(), 33)