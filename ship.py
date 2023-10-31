import pygame

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting Position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect:
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start every dhip st the bottom center of the screen:
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)