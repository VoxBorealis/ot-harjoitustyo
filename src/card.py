import pygame

class Card:
    def __init__(self, surface, id):
        self.surface = surface
        self.id = id
        self.turned_over = False
        self.matched = False

    def get_surface(self):
        return self.surface

    def get_id(self):
        return self.id

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location
    
    def turn_over(self):
        if self.turned_over == False:
            self.turned_over = True
        else:
            self.turned_over = False

    def get_turned_over(self):
        return self.turned_over

    def set_match(self):
        self.matched = True
    
    def get_matched(self):
        return self.matched
