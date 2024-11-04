import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from background import Background
from game_stats import GameStats
from buttons import Button
from scoreboard import ScoreBoard

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
        self.number_of_aliens = self._create_fleet()
        # Tworzenie tła
        self.background = Background(self)
        # Tworzenie instancji statystyk
        self.stats = GameStats(self, self.number_of_aliens)
        # Tworzenie instancji przycisku
        self.play_btn = Button(self, "Play")
        # Tworzenie tablicy wyników
        self.score = ScoreBoard(self)

        # Gra aktywna
        self.game_active = False

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_btn(mouse_pos)
        self._check_collision()
        self._check_aliens_bottom()
        if self.game_active and not self._check_aliens_alive():
            self.game_active = False

    
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

    def _check_collision(self):
        """Sprawdzenie czy zachodzi kolizacja pomiędzy pociskami i obcymi"""
        alien_bullet_coll = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if alien_bullet_coll:
            self.stats.killed_aliens += len(alien_bullet_coll)
            self.stats.aliens_left -= len(alien_bullet_coll)
            print(f"Zabito {self.stats.killed_aliens} obych")
            print(f"Pozostało {self.stats.aliens_left} obych")

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("statek trafiony")
            self.stats.killed_aliens_in_game()
            self._ship_hit()

    def _check_aliens_bottom(self):
        """Sprawdzenie czy obcy przekroczył dolną krawędź"""        
        for alien in self.aliens.sprites():
            if alien.check_bottom():
                self._ship_hit()
                break

    def _check_play_btn(self, mouse_pos):
        """Rozpoczęcie nowej gry po naciśnięciu przycisku"""
        btn_clicked = self.play_btn.rect.collidepoint(mouse_pos)
        if btn_clicked and not self.game_active:
            self.game_active = True
            # Reset statystyk
            self.stats.reset_stats()
            # Zerowanie obcych i pocisków
            self.aliens.empty()
            self.bullets.empty()

            # Tworzenie floty i centrowanie statku
            self._create_fleet()
            self.ship.center_ship()

    def _check_aliens_alive(self):
        """Sprawdzenie czy obcy zostali zabici"""
        return self.aliens.__len__()


    def _update_screen(self):
        """Uaktualnienie obrazów na ekranie"""
        self.screen.fill(self.settings.bg_color)
        self.background.run_background()
        if self.game_active:
            self._update_ship()
            self._update_bullets()
            self._update_fleet()
            self.score.show_score()
        else:
            self.play_btn.draw_btn()

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
            alien.update_position()
            # Jeżeli obcy przy krawędzi -> zmień kierunek
            if alien.check_edges():
                alien.change_direction()

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
        return self.aliens.__len__()

    def _create_alien(self, x_pos, y_pos):
        """Utworzenie obcego"""
        new_alien = Alien(self)
        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos    
        self.aliens.add(new_alien)

    def _ship_hit(self):
        """Reakcja na uderzenie statku"""
        if self.stats.ship_left > 0:
            # Zmniejszenie ilości statków, usunięcie pocisków i obcych
            self.stats.ship_left -= 1
            self.bullets.empty()
            self.aliens.empty()
            self.stats.reset_killed_aliens()

            # Tworzenie nowej floty i środkowanie statku
            self._create_fleet()
            self.ship.center_ship()

            sleep(1)
        else:
            self.game_active = False

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()