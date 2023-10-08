import sys
import pygame

from settings import Settings
from ship import Ship

class SpaceInvaders:
    """ 
    This class manages the overall game assets and game behavior.
    """
    
    def __init__(self):
        """
        Initializes game and game attributes.
        """
        # Initialize Pygame background settings
        pygame.init()
        
        # Instantiate Space Invaders game settings
        self.settings = Settings()
        
        # Set display window. Assign Pygame surface to self.screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invaders")
        
        # Instantiate Pygame clock to maintain frame rate
        self.clock = pygame.time.Clock()
        
        # Instantiate ship, pass in SpaceInvaders instance as argument.
        self.ship = Ship(self)        
        
    def run_game(self):
        """
        Starts game loop, redrawing Pygame surface on every pass and 
        updating screen on each pass.
        """
        while True:
            # Track user actions (event) with event for loop
            for event in pygame.event.get():  # list of events
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw screen each pass of event loop
            self.screen.fill(self.settings.bg_color)
            
            # Draw ship on top of background after background is ready
            self.ship.blitme()
            
            # Makes most recently drawn screen visible, hides old screens
            pygame.display.flip()
            
            # Set game frame rate
            self.clock.tick(60)
    
# Checks if file is called directly or not (ex of not: import as module)
# If run as main program, execute code block
if __name__ == "__main__":
    si = SpaceInvaders()
    si.run_game()