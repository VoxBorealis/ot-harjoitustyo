import pygame

class EventQueue:
    """Luokka, joka vastaa tapahtumienkäsittelystä.
        Käyttää pygamen Event-oliota
    """
    def get(self):
        return pygame.event.get()
