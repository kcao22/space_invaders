import pygame
from settings import Settings

class Ship:
    """
    A class that creates and manages the ship's behavior.
    """
    def __init__(self, si_game):
        """
        Initializes ship and sets starting position.
        """
        # All game elements in Pygame are rectangles
        # Access rectangles to place / position objects in game
        # Access game screen resources as defined in SpaceInvaders
        # Get screen's rectangle
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        
        # Image returns surface representing ship
        # Get ship's surface rectangle
        # Set ship to middle bottom of game screen
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Set placeholder x and y positions as floats. Use to update rect
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Flag for continuous movements. If True, continuously += 1 pos
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # Access settings for ship speed
        self.settings = Settings()
        
        
    def blitme(self):
        """
        Draws ship at current location.
        """
        # Draws image to game screen at specified position by self.rect
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """
        Checks if continuous movement flag. Update position accordingly.
        """
        # Iterate x, y based on flag
        # If instead of elif to avoid single key registering only
        # Ex: elif will prioritize right key if left and right are pushed
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        if self.moving_up:
            self.y -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed
        
        # Update position of rectangle after iteration
        self.rect.x = self.x
        self.rect.y = self.y