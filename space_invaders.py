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
            # Check game events for quit action.
            self._check_events()
            
            # Update screen on each pass of loop
            self._update_screen()
            
            # Set game frame rate
            self.clock.tick(60)
    
    def _check_events(self):
        """
        Responds to keypresses and mouse clicks; checks if quit.
        """
        # Track user actions (event) with event for loop
        for event in pygame.event.get():  # list of events
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """
        Updates images on the screen and flips to new screen.
        """
        # Fill screen background
        self.screen.fill(self.settings.bg_color)
        
        # Draw ship on top of background after background is ready at 
        # specific position
        self.ship.blitme()
        
        # Makes most recently drawn screen visible, hides old screens
        pygame.display.flip()
    
# Checks if file is called directly or not (ex of not: import as module)
# If run as main program, execute code block
if __name__ == "__main__":
    si = SpaceInvaders()
    si.run_game()