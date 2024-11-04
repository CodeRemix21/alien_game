import pygame

class Ship:
    """Klasa przeznaczona do zarządzania statkiem"""

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe"""
        # Atrybut settings
        self.settings = ai_game.settings

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytanie obrazu statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship_T.png')
        self.rect = self.image.get_rect()

        # Statek pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        # Poruszanie statkiem w prawo
        self.move_right = False

        # Poruszanie statkiem w lewo
        self.move_left = False

    def blitme(self):
        """Wyświetlenie statku kosmicznego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        """Aktualizacja pozycji statku na ekranie"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        
        if self.move_left and self.rect.left > 0:   
            self.rect.x -= self.settings.ship_speed

    def center_ship(self):
        """Pozycjonowanie statku do pozycji początkowej"""
        self.rect.midbottom = self.screen_rect.midbottom