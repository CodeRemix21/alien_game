import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa przeznaczona do zarządzania pociskami"""

    def __init__(self, ai_game):
        """Utworzenie obiektu pocisku w aktualnym położeniu statku"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Wczytanie obrazu pocisku i pobranie jego prostokąta
        self.image = pygame.image.load('images/bullet_T.png')
        self.rect = self.image.get_rect()

        # Pocisk pojawia się na górze statku
        self.rect.midbottom = ai_game.ship.rect.midtop

    def blitme(self):
        """Wyświetlenie pocisku w jego położeniu"""        
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        """Aktualizacja pozycji pocisku"""
        self.rect.y -= self.settings.bullet_speed