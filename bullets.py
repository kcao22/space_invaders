import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, si_game):
        """
        A class that creates and manages bullets fired from the user's ship.
        """
        # Call sprite parent class constructor
        super().__init__()
        
        # Set screen attributes
        self.screen = si_game.screen
        self.settings = si_game.settings
        self.color = si_game.settings.bullet_color

        # Create bullet 