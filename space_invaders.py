import sys

import pygame

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
        
        # Set display window. Assign Pygame surface to self.screen
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Space Invaders")
        
        # Instantiate Pygame clock to maintain frame rate
        self.clock = pygame.time.Clock()
        
        # Set background color to gray
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """
        Starts game loop, redrawing Pygame surface on every pass and 
        updating screen on each pass.
        """
        while True:
            # Track user actions (event) with event for loop
            for event in pygame.event.get():  # list of events
                if event.type == event.QUIT:
                    sys.exit()
            
            # Redraw screen each pass of event loop
            self.screen.fill(self.bg_color)
            
            # Makes most recently drawn screen visible, hides old screens
            pygame.display.flip()
            # Set game frame rate
            self.clock.tick(60)
    
# Checks if file is called directly or not (ex of not: import as module)
# If run as main program, execute code block
if __name__ == "__main__":
    si = SpaceInvaders()
    si.run_game()