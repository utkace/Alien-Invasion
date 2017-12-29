import pygame
from pygame.sprite import Sprite

class Ship_left(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        super(Ship_left, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship_left_icon.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

