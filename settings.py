class Settings:
    """
    A class to store the settings of Space Invaders.
    """
    def __init__(self):
        """
        Initialize game settings.
        """
        # Screen and surface settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Ship speed setting
        self.ship_speed = 6
        