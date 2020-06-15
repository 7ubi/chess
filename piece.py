import pygame

pygame.init()


class Piece:

	def __init__(self, color, x, y, w, h):
		self.color = color
		self.x = x
		self.y = y
		self.selected = False
		self.w = int(w)
		self.h = int(h)
		self.blackImg
		self.whiteImg

	def setSelected(self, set):
		self.selected = set

	def check(self, x, y):
		pass

	def clickedOn(self, pos):
		x, y = pos
		if x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h:
			return True
		return False

	def move(self, pos, field, width, height):
		nx, ny = pos
		if self.selected:
			x = int(nx / self.w) * self.w
			y = int(ny / self.h) * self.h
    		
			canBePlaced = self.check(x, y)

			if field[int(x / width * 8)][int(y / height * 8)] == self.color:
				return False

			if canBePlaced:
				self.x = x
				self.y = y
				return True



	def show(self, screen):
		if self.selected:
			pygame.draw.rect(screen, pygame.Color(255, 0, 0), (self.x, self.y, self.w, self.h))


		if self.color == 1:
			screen.blit(pygame.transform.scale(self.blackImg, (self.w, self.h)), (self.x, self.y))

		if self.color == -1:
			screen.blit(pygame.transform.scale(self.whiteImg, (self.w, self.h)), (self.x, self.y))


