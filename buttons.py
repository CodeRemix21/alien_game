import pygame.font

class Button:
    """Klasa do tworzenia przycisków dla gry"""

    def __init__(self, ai_game, msg):
        """Inicjalizacja atrybutów przycisku"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        # Wymiary i właściwości przycisku
        self.width, self.height = 200, 50
        self.font = pygame.font.SysFont(None, 48)

        # Utworzenie prostokąta i wyśrodkowanie go
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.rect.center = self.screen_rect.center

        # Komunikat wyświetlany przez przycisk
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Umieszczenie komunikatu w wygenerowanym obrazie"""
        self.msg_img = self.font.render(msg, True, self.settings.text_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_btn(self):
        """Wyświetlenie przycisku"""
        self.screen.blit(self.surface, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)