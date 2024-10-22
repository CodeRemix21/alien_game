import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Klasa ogólna przeznaczona do zarządzania zasobami i sposobem dzialania gry"""

    def __init__(self):
        """Inicjalizacja gry"""
        # Tworzenie instancji ustawień do gry
        self.settings = Settings()

        # Ustawienia        
        pygame.init()
        pygame.display.set_caption(self.settings.title)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Tworzenie instancji statku
        self.ship = Ship(self)

    def run_game(self):
        """Rozpoczęcie gry"""
        while True:
            self._check_events()
            self._update_sreen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        """Reakcja na zdarzenia generowane przez użytkownika"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
    
    def _check_keydown_event(self, event: pygame.event):
        """Reakcja na uopuszczenie klawisza"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True

    def _check_keyup_event(self, event: pygame.event):
        """Reakcja na naciśnięcie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _update_sreen(self):
        """Uaktualnienie obrazów na ekranie"""
        self.ship.update_position()
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()