import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przeznaczona do zarządzania obcymi"""
    def __init__(self, ai_game):
        """Inicjalizacja obcego i zdefiniowanie jego położenia"""
        super().__init__()
        self.screen = ai_game.screen

        # Wczytanie obrazu obcego i pobranie jego prostokąta
        self.image = pygame.image.load('images/alien_T.png')
        self.rect = self.image.get_rect()

        # Obcy pojawia się w lewym górnym rogu
        self.rect.y = self.rect.height
    
    def blitme(self):
        """Wyświetlenie obcego w jego położeniu"""
        self.screen.blit(self.image, self.rect)

    def set_position_xy(self, x, y):
        self.rect.x = x
        self.rect.y = y