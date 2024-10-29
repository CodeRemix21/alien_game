import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from background import Background

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
        # Tworzenie instancji pocisków
        self.bullets = pygame.sprite.Group()
        # Tworzenie instancji obcych i ich floty
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Tworzenie tła
        self.background = Background(self)

    def run_game(self):
        """Rozpoczęcie gry"""
        while True:
            self._check_events()
            self._update_screen()
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
        """Reakcja na upuszczenie klawisza"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.move_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event: pygame.event):
        """Reakcja na naciśnięcie klawisza"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie"""
        self.screen.fill(self.settings.bg_color)
        self.background.run_background()
        self._update_ship()
        self._update_bullets()
        self._update_fleet()

        pygame.display.flip()

    def _update_ship(self):
        """Uaktualnienie statku na ekranie"""
        self.ship.update_position()
        self.ship.blitme()
    
    def _update_bullets(self):
        """Uaktualnienie pocisków na ekranie"""
        for bullet in self.bullets.sprites():
            bullet.update_position()
            bullet.blitme()
            # Jeżeli pocisk poza ekranem -> usuń
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)

    def _update_fleet(self):
        """Uaktualnieie obych na ekranie"""
        for alien in self.aliens.sprites():
            alien.blitme()

    def _fire_bullet(self):
        """Utworzenie nowego pocisku i dodanie do grupy"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Utworzenie floty obcych"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_y = alien_height
        row_nr = 0

        while current_y < (self.settings.screen_height - 8 * alien_height):
            row_nr += 1
            current_x = 2 * alien_width if row_nr % 2 == 0 else alien_width
            
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_pos, y_pos):
        """Utworzenie obcego"""
        new_alien = Alien(self)
        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos    
        self.aliens.add(new_alien)

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()