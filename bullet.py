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
        self.color = self.settings.bullet_color

        # Create bullet rectangle
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # Set bullet position
        self.rect.midtop = si_game.ship.rect.midtop
        # Store bullet position for position updating
        self.y = float(self.rect.y)
        
    def update(self):
        """
        Updates bullet y-axis position on screen.
        """
        # Update position tracking instance variable
        self.y -= self.settings.bullet_speed
        # Update bullet actual position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """ 
        Draws bullet to screen.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    