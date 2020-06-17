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

            canBePlaced = self.canBePlaced(x, y, field)

            if field[int(x / width * 8)][int(y / height * 8)] == self.color:
                return False

            if canBePlaced:
                self.x = x
                self.y = y
                return True

    def horverMove(self, x, y, field):
        if self.y == y:
            d = self.x - x
            i = int(self.x / (self.w * 8) * 8)
            j = int(x / (self.w * 8) * 8)
            m = int(self.y / (self.h * 8) * 8)
            print(d)
            if d < 0:
                i += 1
                for k in range(i, j, 1):
                    if field[int(k)][m] != 0:
                        return False
            else:
                i -= 1
                for k in range(i, j, -1):
                    if field[int(k)][m] != 0:
                        return False

            return True

        if self.x == x:
            d = self.y - y
            i = int(self.y / (self.h * 8) * 8)
            j = int(y / (self.h * 8) * 8)
            m = int(self.x / (self.w * 8) * 8)
            if d < 0:
                i += 1
                for k in range(i, j, 1):
                	print(field[m][k])
                	if field[m][k] != 0:
                		return False
            else:
                i -= 1
                for k in range(i, j, -1):
                	print(field[m][k])
                	if field[m][k] != 0:
                		return False

            return True
        return False

    def show(self, screen):
        if self.selected:
            pygame.draw.rect(screen, pygame.Color(255, 0, 0),
                             (self.x, self.y, self.w, self.h))

        if self.color == 1:
            screen.blit(pygame.transform.scale(
                self.blackImg, (self.w, self.h)), (self.x, self.y))

        if self.color == -1:
            screen.blit(pygame.transform.scale(
                self.whiteImg, (self.w, self.h)), (self.x, self.y))
