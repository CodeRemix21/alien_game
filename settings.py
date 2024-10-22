class Settings():
    """Klasa przeznaczona do przechowywania ustawień gry"""
    
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu
        self.title = "Inwazja obcych"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia statku
        self.ship_speed = 5

        # Ustawienia pocisku
        self.bullet_speed = 10
        self.bullets_allowed = 5

        # FPS
        self.fps = 60