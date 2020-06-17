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

bishop_black = pygame.image.load(os.path.join('data', 'bishop_black.png')) 
bishop_white = pygame.image.load(os.path.join('data', 'bishop_white.png')) 

class Rook(Piece):
    def __init__(self, color, x, y, w, h):
        self.blackImg = rook_black
        self.whiteImg = rook_white
        super().__init__(color, x, y, w, h)

    def canBePlaced(self, x, y, field):
    	return self.horverMove(x, y, field)
    	return False

class Bishop(Piece):
	def __init__(self, color, x, y, w, h):
		self.blackImg = bishop_black
		self.whiteImg = bishop_white
		super().__init__(color, x, y, w, h)

	def canBePlaced(self, x, y, field):
		distX = abs(self.x - x)
		distY = abs(self.y - y)
		
		if int(distX) == int(distY):
			return True
		return False     

class King(Piece):
	def __init__(self, color, x, y, w, h):
		self.blackImg = king_black
		self.whiteImg = king_white
		super().__init__(color, x, y, w, h)

	def canBePlaced(self, x, y, field):
		distX = abs(self.x - x) / self.w
		distY = abs(self.y - y) / self.h

		if int(distX) == 0 or int(distX) == 1:
			if int(distY) == 0 or int(distY) == 1:
				return True
		return False

class Queen(Piece):
	def __init__(self, color, x, y, w, h):
		self.blackImg = queen_black
		self.whiteImg = queen_white
		super().__init__(color, x, y, w, h)

	def canBePlaced(self, x, y, field):
		distX = abs(self.x - x)
		distY = abs(self.y - y)

		if int(distX) == int(distY):
			return True

		return self.horverMove(x, y, field)

		return False

class Knight(Piece):
	def __init__(self, color, x, y, w, h):
		self.blackImg = knight_black
		self.whiteImg = knight_white
		super().__init__(color, x, y, w, h)

	def canBePlaced(self, x, y, field):
		distX = abs(self.x - x) / self.w
		distY = abs(self.y - y) / self.h

		if distX == 2 or distY == 2:
			if distX == 1 or distY == 1:
				return True
		return False

class Pawn(Piece):
	def __init__(self, color, x, y, w, h):
		self.blackImg = pawn_black
		self.whiteImg = pawn_white
		self.startX = x
		self.startY = y
		super().__init__(color, x, y, w, h)

	def canBePlaced(self, x, y, field):
		i = int(self.x / self.w * 8 * 8)
		j = int(self.y / self.h * 8 * 8)

		distX = (self.x - x) / self.w
		distY = abs(self.y - y) / self.h

		if self.x == self.startX and self.y == self.startY:
			if distY == 2 and distX == 0:
				return True

		if distY == 1 and distX == 0:
			return True

		return False