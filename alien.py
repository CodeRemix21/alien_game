import pygame
from pygame.sprite import Sprite
#
class Alien(Sprite):
    """Klasa przeznaczona do zarządzania obcymi"""
    def __init__(self, ai_game):
        """Inicjalizacja obcego i zdefiniowanie jego położenia"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Wczytanie obrazu obcego i pobranie jego prostokąta
        self.image = pygame.image.load('images/alien_T.png')
        self.rect = self.image.get_rect()

        # Obcy pojawia się w lewym górnym rogu
        self.rect.y = self.rect.height

        # 1 - kierunek w prawo, -1 - kierunek w lewo
        self.direction = 1
    
    def blitme(self):
        """Wyświetlenie obcego w jego położeniu"""
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        """Aktualizacja pozycji obcego na ekranie"""
        self.rect.x += self.settings.alien_speed * self.direction
        self.rect.y += self.settings.fleet_drop_speed

    def check_edges(self):
        """Zwraca True jeżeli obcy jest przy krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def check_bottom(self):
        """Zwraca True jeżeli obcy przekroczy dolną krawędź"""
        return self.rect.bottom >= self.settings.screen_height
    
    def change_direction(self):
        """Zmiana kierunku ruchu"""
        self.direction *= -1
