import pygame

class Ship:
    """
    A class that creates and manages the ship's behavior.
    """
    def __init__(self, si_game):
        """
        Initializes ship and sets starting position.
        """
        # All game elements in Pygame are rectangles.
        # Access rectangles to place / position objects in game.
        # Access game screen resources as defined in SpaceInvaders.
        # Get screen's rectangle.
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        
        # Image returns surface representing ship.
        # Get ship's surface rectangle. 
        # Set ship to middle bottom of game screen.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Flag for continuous movements. If True, continuously += 1 pos.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def blitme(self):
        """
        Draws ship at current location.
        """
        # Draws image to game screen at specified position by self.rect.
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """
        Checks if continuous movement flag. Update position accordingly.
        """
        # If moving_right, iterate ship rectangle position to right once.
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.y += 1
        if self.moving_up:
            self.rect.top += 1
        if self.moving_down:
            self.rect.bottom += 1