class GameStats:
    """Monitorowanie danych statystycznych w grze"""
    def __init__(self, ai_game, all_aliens):
        """Inicjalizacja danych"""
        self.settings = ai_game.settings
        self.all_aliens = all_aliens
        self.reset_stats()

    def reset_stats(self):
        """Resetowanie danych"""
        self.ship_left = self.settings.ship_limit
        self.all_killed_aliens = []
        self.killed_aliens = 0
        self.aliens_left = self.all_aliens

    def killed_aliens_in_game(self):
        """Zapis ilości zabitych obcych do tablicy"""
        self.all_killed_aliens.append(self.killed_aliens)

    def reset_killed_aliens(self):
        """Resetowanie zabitych obcych w grze"""
        self.killed_aliens = 0
        self.aliens_left = self.all_aliens