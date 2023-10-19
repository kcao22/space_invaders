import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
            
        pygame.display.set_caption("Space Invaders")
        
        # Instantiate Pygame clock to maintain frame rate
        self.clock = pygame.time.Clock()
        
        # Instantiate ship, pass in SpaceInvaders instance as argument.
        self.ship = Ship(self)        

        # Instance variable for grouping bullets
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """
        Starts game loop, redrawing Pygame surface on every pass and 
        updating screen on each pass.
        """
        while True:
            # Check game events and respond accordingly to event.
            self._check_events()
            self.ship.update()
            self._update_bullets()

            # Check to see if bullets are out of screen. Delete if true
            # Create copy to avoid in place changes during loop
            # Modify original self.bullets list based on copy
            for bullet in self.bullets.copy():
                if bullet.rect.bottom < 0:
                    self.bullets.remove(bullet)
                else:
                    pass
            print(len(self.bullets))

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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
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
        if event.key == pygame.K_q:
            sys.quit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
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

    def _update_bullets(self):
        """
        Updates bullet positioning and gets rid of bullets out of screen
        """
        # Update bullet positioning
        self.bullets.update()



    def _update_screen(self):
        """
        Updates images on the screen and flips to new screen.
        """
        # Fill screen background
        self.screen.fill(self.settings.bg_color)

        # Draw all bullets grouped in sprite list. Draw bullets first to
        # avoid drawing bullets on top of ship
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # Draw ship on top of background after background is ready at 
        # specific position
        self.ship.blitme()
        
        # Makes most recently drawn screen visible, hides old screens
        pygame.display.flip()

    def _fire_bullet(self):
        """
        Creates bullet object and appends to bullet sprite group
        for tracking.
        """
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        else:
            pass    
# Checks if file is called directly or not (ex of not: import as module)
# If run as main program, execute code block
if __name__ == "__main__":
    si = SpaceInvaders()
    si.run_game()