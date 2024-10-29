import pygame

class Background:
    """Klasa do utworzenia tła gry"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Wczytanie obrazu tła
        self.image = pygame.image.load('images/bg.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.screen_width, self.settings.screen_height))
        self.rect = self.image.get_rect()
        self.dist_y = 0
        

    def run_background(self):
        """Efekt poruszającego się tła"""
        tiles = 2
        i = 0

        while i < tiles:
              self.screen.blit(self.image, (0, -self.rect.height*i+self.dist_y))
              i += 1
        
        self.dist_y += self.settings.background_speed
        if self.dist_y > self.rect.height:
             self.dist_y = 0