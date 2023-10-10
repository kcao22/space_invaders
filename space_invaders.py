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
            # Check game events and respond accordingly to event.
            self._check_events()
            self.ship.update()
            
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
            # If user quits, exit game
            if event.type == pygame.QUIT:
                sys.exit()
            # If keypress action, respond accordingly
            # Allow for continuous action by tracking keydown & keyup
            elif event.type == pygame.KEYDOWN:
                # If right arrow key, shift ship rectangle 1 unit right
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
                
    def check_keydown_events(self, event):
        """
        Responds to key presses accordingly.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def check_keyup_events(self, event):
        """
        Responds to key releases accordingly. 
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

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