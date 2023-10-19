import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    Alien class representing a single alien craft.
    """
    def __init__(self, si_game):
        """
        Initializes alien at starting position.
        """
        # Call sprite parent constructor
        super().__init__()
        
        # Set screen
        self.screen = si_game.screen
        
        # Image returns surface representing ship
        # Get alien's surface rectangle
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Set alien position