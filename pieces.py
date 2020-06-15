import pygame
import os
from piece import Piece

pygame.init()

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

class Rook(Piece):
    def __init__(self, color, x, y, w, h):
        self.blackImg = rook_black
        self.whiteImg = rook_white
        super().__init__(color, x, y, w, h)

    def check(self, x, y):
    	if self.x == x or self.y == y:
    		return True
    	return False

bishop_black = pygame.image.load(os.path.join('data', 'bishop_black.png')) 
bishop_white = pygame.image.load(os.path.join('data', 'bishop_white.png')) 


class Bishop(Piece):
	def __init__(self, color, x, y, w, h):
		self.blackImg = bishop_black
		self.whiteImg = bishop_white
		super().__init__(color, x, y, w, h)

	def check(self, x, y):
		distX = abs(self.x - x)
		distY = abs(self.y - y)
		
		if int(distX) == int(distY):
			return True
		return False     