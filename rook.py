import pygame
import os

pygame.init()

bishop_black = pygame.image.load(os.path.join('data', 'bishop_black.png')) 
bishop_white = pygame.image.load(os.path.join('data', 'bishop_white.png')) 

king_black = pygame.image.load(os.path.join('data', 'king_black.png')) 
king_white = pygame.image.load(os.path.join('data', 'king_white.png')) 

knight_black = pygame.image.load(os.path.join('data', 'knight_black.png')) 
knight_white = pygame.image.load(os.path.join('data', 'knight_white.png')) 

pawn_black = pygame.image.load(os.path.join('data', 'pawn_black.png')) 
pawn_white = pygame.image.load(os.path.join('data', 'pawn_white.png')) 

queen_black = pygame.image.load(os.path.join('data', 'queen_black.png')) 
queen_white = pygame.image.load(os.path.join('data', 'queen_white.png')) 

rook_black = pygame.image.load(os.path.join('data', 'rook_black.png')) 
rook_white = pygame.image.load(os.path.join('data', 'rook_white.png')) 

class Rook:
    def __init__(self, color, x, y, w, h):
        self.color = color
        self.x = x
        self.y = y
        self.selected = False
        self.w = int(w)
        self.h = int(h)

    def setSelected(self, set):
    	self.selected = set

    def clickedOn(self, pos):
    	x, y = pos
    	if x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h:
    		return True
    	return False

    def check(self, x, y):
    	if self.x == x or self.y == y:
    		return True
    	return False

    def move(self, pos, field, width, height):
    	nx, ny = pos
    	if self.selected:
    		x = int(nx / self.w) * self.w
    		y = int(ny / self.h) * self.h
    		
    		canBePlaced = self.check(x, y)

    		if field[int(x / width * 8)][int(y / height * 8)] == self.color:
    			return

    		if canBePlaced:
    			self.x = x
    			self.y = y



    def show(self, screen, width, height):
    	if self.selected:
    		pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.x, self.y, self.w, self.h))


    	if self.color == 1:
    		screen.blit(pygame.transform.scale(rook_black, (self.w, self.h)), (self.x, self.y))

    	if self.color == -1:
    		screen.blit(pygame.transform.scale(rook_white, (self.w, self.h)), (self.x, self.y))




        