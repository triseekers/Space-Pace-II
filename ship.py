import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		#initialize ship & set its starting position
		super(Ship, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#load image and rect.
		self.image = pygame.image.load('images/new.PNG')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#start new ship at bottom center of the scren
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
		#movement flag
		self.moving_right = False
		self.moving_left = False

	def center_ship(self):
		#center the ship on the screen
		self.center = self.screen_rect.centerx

	def update(self):
		#update the ship's position based on the movement flag
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		#update rect object from self.center
		self.rect.centerx = self.center
		
	def blitme(self):
		#draw the ship on current location
		self.screen.blit(self.image, self.rect)