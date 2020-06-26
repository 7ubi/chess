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
    def __init__(self, color, x, y, w, h, score):
        self.blackImg = rook_black
        self.whiteImg = rook_white
        super().__init__(color, x, y, w, h, score)
    def showAllMoves(self, field, screen):
    	if self.selected:
    		self.showHorVerMove(field, screen)

    def getAllMoves(self, field):
    	self.getHorVerMove(field)

    def canBePlaced(self, x, y, field):
    	return self.horverMove(x, y, field)
    	return False

class Bishop(Piece):
	def __init__(self, color, x, y, w, h, score):
		self.blackImg = bishop_black
		self.whiteImg = bishop_white
		super().__init__(color, x, y, w, h, score)

	def showAllMoves(self, field, screen):
		if self.selected:
			self.showAllCrossMoves(field, screen)

	def canBePlaced(self, x, y, field):
		if self.crossMove(x, y, field):
			return True
		return False
		

class King(Piece):
	def __init__(self, color, x, y, w, h, score):
		self.blackImg = king_black
		self.whiteImg = king_white
		super().__init__(color, x, y, w, h, score)
	
	def showAllMoves(self, field, screen):
		if self.selected:
			k = int(self.x / (self.w * 8) * 8)
			m = int(self.y / (self.h * 8) * 8)
			for i in range(-1, 2):
				for j in range(-1, 2):
					if k + i < 0 or k + i > 7 or m + j < 0 or m + j > 7:
						continue
					if field[k + i][m + j] != self.color:
						self.drawRectWithAlpha(0, 255, 0, 100, self.x + self.w * i, self.y + self.h * j, screen)
	
	def getAllMoves(self, field):
		k = int(self.x / (self.w * 8) * 8)
		m = int(self.y / (self.h * 8) * 8)
		for i in range(-1, 2):
			for j in range(-1, 2):
				if k + i < 0 or k + i > 7 or m + j < 0 or m + j > 7:
					continue
				if field[k + i][m + j] != self.color:
					self.allMoves.append([(k + i) * self.w, (m + j) * self.h])

	def canBePlaced(self, x, y, field):
		distX = abs(self.x - x) / self.w
		distY = abs(self.y - y) / self.h

		if int(distX) == 0 or int(distX) == 1:
			if int(distY) == 0 or int(distY) == 1:
				return True
		return False

class Queen(Piece):
	def __init__(self, color, x, y, w, h, score):
		self.blackImg = queen_black
		self.whiteImg = queen_white
		super().__init__(color, x, y, w, h, score)

	def showAllMoves(self, field, screen):
		if self.selected:
			self.showHorVerMove(field, screen)
			self.showAllCrossMoves(field, screen)

	def getAllMoves(self, field):
		self.getAllCrossMoves(field)
		self.getHorVerMove(field)

	def canBePlaced(self, x, y, field):
		if self.crossMove(x, y, field):
			return True

		return self.horverMove(x, y, field)

		return False

class Knight(Piece):
	def __init__(self, color, x, y, w, h, score):
		self.blackImg = knight_black
		self.whiteImg = knight_white
		super().__init__(color, x, y, w, h, score)

	def showAllMoves(self, field, screen):
		if self.selected:
			i = int(self.x / (self.w * 8) * 8)
			j = int(self.y / (self.h * 8) * 8)
			for k in range(-2, 3, 4):
				for m in range(-1, 2, 2):
					if i + k >= 0 and i + k <= 7:
						if j + m >= 0 and j + m <= 7:
							if field[i + k][j + m] != self.color:
								self.drawRectWithAlpha(0, 255, 0, 100, self.w * (i + k), self.h * (j + m), screen)
					
					if i + m >= 0 and i + m <= 7: 
						if j + k >= 0 and j + k <= 7:
							if field[i + m][j + k] != self.color:
								self.drawRectWithAlpha(0, 255, 0, 100, self.w * (i + m), self.h * (j + k), screen)

	def getAllMoves(self, field):
		i = int(self.x / (self.w * 8) * 8)
		j = int(self.y / (self.h * 8) * 8)
		for k in range(-2, 3, 4):
			for m in range(-1, 2, 2):
				if i + k >= 0 and i + k <= 7:
					if j + m >= 0 and j + m <= 7:
						if field[i + k][j + m] != self.color:
							self.allMoves.append([(i + k) * self.w, (j + m) * self.h])
					
				if i + m >= 0 and i + m <= 7: 
					if j + k >= 0 and j + k <= 7:
						if field[i + m][j + k] != self.color:
							self.allMoves.append([(i + m) * self.w, (j + k) * self.h])

	def canBePlaced(self, x, y, field):
		distX = abs(self.x - x) / self.w
		distY = abs(self.y - y) / self.h

		if distX == 2 or distY == 2:
			if distX == 1 or distY == 1:
				return True
		return False

class Pawn(Piece):
	def __init__(self, color, x, y, w, h, score):
		self.blackImg = pawn_black
		self.whiteImg = pawn_white
		self.startX = x
		self.startY = y
		super().__init__(color, x, y, w, h, score)

	def showAllMoves(self, field, screen):
		if not self.selected:
			return

		i = int(self.x / (self.w * 8) * 8)
		j = int(self.y / (self.h * 8) * 8)

		for k in range(-1, 2, 2):
			if i + k < 0 or i + k > 7:
				continue

			if field[i + k][j + self.color] == -self.color:
				self.drawRectWithAlpha(0, 255, 0, 100, self.w * (i + k), self.h * (j + self.color), screen)
	
		if field[i][j + self.color] == 0:
			self.drawRectWithAlpha(0, 255, 0, 100, self.w * i, self.h * (j + self.color), screen)
		else:
			return

		ny = (j + (2 * self.color)) * self.h 
		if self.y == self.startY:
			if field[i][j + (self.color * 2)] == 0:
				self.drawRectWithAlpha(0, 255, 0, 100, self.w * i, ny, screen)

	def getAllMoves(self, field):
		i = int(self.x / (self.w * 8) * 8)
		j = int(self.y / (self.h * 8) * 8)

		for k in range(-1, 2, 2):
			if i + k < 0 or i + k > 7:
				continue

			if field[i + k][j + self.color] == -self.color:
				self.allMoves.append([(i + k) * self.w, (j + self.color) * self.h])
	
		if field[i][j + self.color] == 0:
			self.allMoves.append([(i) * self.w, (j + self.color) * self.h])
		else:
			return

		ny = (j + (2 * self.color)) * self.h 
		if self.y == self.startY:
			if field[i][j + (self.color * 2)] == 0:
				self.allMoves.append([(i) * self.w, ny])


	def showAllMoves(self, field, screen):
		if not self.selected:
			return

		i = int(self.x / (self.w * 8) * 8)
		j = int(self.y / (self.h * 8) * 8)

		for k in range(-1, 2, 2):
			if i + k < 0 or i + k > 7:
				continue

			if field[i + k][j + self.color] == -self.color:
				self.drawRectWithAlpha(0, 255, 0, 100, self.w * (i + k), self.h * (j + self.color), screen)
	
		if field[i][j + self.color] == 0:
			self.drawRectWithAlpha(0, 255, 0, 100, self.w * i, self.h * (j + self.color), screen)
		else:
			return

		ny = (j + (2 * self.color)) * self.h 
		if self.y == self.startY:
			if field[i][j + (self.color * 2)] == 0:
				self.drawRectWithAlpha(0, 255, 0, 100, self.w * i, ny, screen)

	def canBePlaced(self, x, y, field):
		i = int(x / (self.w * 8) * 8)
		j = int(y / (self.h * 8) * 8)

		distX = (self.x - x) / self.w
		distY = (self.y - y) / self.h

		if self.x == self.startX and self.y == self.startY:
			if int(distY) == -self.color * 2 and int(distX) == 0 and field[i][j] == 0:
				return True

		if int(distY) == -self.color and int(distX) == 0 and field[i][j] == 0:
			return True

		if abs(distX) == 1 and int(distY) == -self.color:
			if field[i][j] == -self.color:
				return True

		return False