import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Klasa ogólna przeznaczona do zarządzania zasobami i sposobem dzialania gry"""

    def __init__(self):
        """Tworzenie instancji ustawień do gry"""
        self.settings = Settings()

        """Inicjalizacja gry"""
        pygame.init()
        pygame.display.set_caption(self.settings.title)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        """Rozpoczęcie gry"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(self.settings.fps)


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()