class Settings():
    """Klasa przeznaczona do przechowywania ustawień gry"""
    
    def __init__(self):
        """Inicjalizacja ustawień gry"""
        # Ustawienia ekranu
        self.title = "Inwazja obcych"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # FPS
        self.fps = 60