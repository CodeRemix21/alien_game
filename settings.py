class Settings():
    """Klasa przeznaczona do przechowywania ustawień gry"""
    
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu
        self.title = "Inwazja obcych"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.background_speed = 2

        # Ustawienia statku
        self.ship_speed = 5
        self.ship_limit = 3

        # Ustawienia pocisku
        self.bullet_speed = 10
        self.bullets_allowed = 10

        # Ustawienia obcego
        self.alien_speed = 2
        self.fleet_drop_speed = 0.75

        # FPS
        self.fps = 60