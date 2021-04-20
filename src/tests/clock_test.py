import unittest
import pygame

from clock import Clock

class testClock(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

    def test_tick_toimii(self):
        i = 0
        while i <= 10:
            self.clock.tick(30)
            i+=1
        self.assertEqual(int(self.clock._clock.get_fps()), 30)

    def test_get_ticks_toimii(self):
        self.clock.tick(30)
        self.assertEqual(self.clock.get_ticks(), 33)