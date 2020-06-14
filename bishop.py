import pygame
import os

pygame.init()

bishop_black = pygame.image.load(os.path.join('data', 'bishop_black.png')) 
bishop_white = pygame.image.load(os.path.join('data', 'bishop_white.png')) 

class Bishop:
	def __init__(self, color, x, y, w, h):
		self.color = color
		self.x = x
		self.y = y
		self.w = int(w)
		self.h = int(h)
		self.selected = False

	def show(self, screen):
		if self.selected:
			pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.x, self.y, self.w, self.h))

		if self.color == 1:
			screen.blit(pygame.transform.scale(bishop_black, (self.w, self.h)), (self.x, self.y))
		else:
			screen.blit(pygame.transform.scale(bishop_white, (self.w, self.h)), (self.x, self.y))