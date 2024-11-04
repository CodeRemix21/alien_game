import pygame

class ScoreBoard:
    """Klasa do stworzenia tablicy ze statystykami"""

    def __init__(self, ai_game):
        """Inicjalizacja atrybutów dla tablicy"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = ai_game.stats
        self.settings = ai_game.settings

        # Ustawienie czcionki
        self.font = pygame.font.SysFont(None, 24)

        # Przygotowanie punktacji
        self.prep_score()

        # Wyświetlenie punktacji w prawym górnym rogu
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_score(self):
        """Przekształcenie punktacji na obraz"""
        score_str = "Aliens left: " + str(self.stats.aliens_left)
        self.score_img = self.font.render(score_str, True, self.settings.text_color)

    def show_score(self):
        """Wyświetlenie punktacji"""
        self.prep_score()
        self.screen.blit(self.score_img, self.score_rect)