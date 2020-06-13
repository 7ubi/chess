import pygame
import os
import sys
from rook import Rook

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess")

clock = pygame.time.Clock()

field = [[0 for x in range(8)] for y in range(8)]

rook_black = [Rook(1, 0, 0, width/8, height/8), Rook(1, 7 * width/8, 0, width / 8, height/8)]

rook_white = [Rook(-1, 0, 7 * height / 8, width/8, height/8), Rook(-1, 7 * width / 8, 7 * height / 8, width/8, height/8)]

def defPlayingField(): #black = 1 white = -1 nothing = 0
    global field
    field = [[0 for x in range(8)] for y in range(8)]

    for i in range(len(rook_black)):
        field[int(rook_black[i].x / width * 8)][int(rook_black[i].y / height * 8)] = 1

def drawBoard():
    for i in range(8):
        for j in range(8):
            if (j + i) % 2 == 0:
                pygame.draw.rect(screen, pygame.Color(102, 51, 0), (int(j * width/8), int(i * height/8), int(width/8), int(height/8)))
            else:
                pygame.draw.rect(screen, pygame.Color(153, 102, 51), (int(j * width/8), int(i * height/8), int(width/8), int(height/8)))

def deselectAll(c):
    if c == 'black':
        for i in range(len(rook_black)):
            rook_black[i].setSelected(False)

    if c == 'white':
        for i in range(len(rook_white)):
            rook_white[i].setSelected(False)


def main():
    while True:
        defPlayingField()
        # print(field)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(rook_black)):
                    if rook_black[i].clickedOn(pygame.mouse.get_pos()):
                        deselectAll('black')
                        rook_black[i].setSelected(True)

                    x, y = pygame.mouse.get_pos()
                    w, h = width/8, height/8
                    x = int(x / w) * w
                    y = int(y / h) * h

                    if rook_black[i].selected:
                        if rook_black[i].x != x or rook_black[i].y != y:

                            rook_black[i].move(pygame.mouse.get_pos(), field, width, height)
                            deselectAll('black')
                for i in range(len(rook_white)):
                    if rook_white[i].clickedOn(pygame.mouse.get_pos()):
                        deselectAll('white')
                        rook_white[i].setSelected(True)

                    x, y = pygame.mouse.get_pos()
                    w, h = width/8, height/8
                    x = int(x / w) * w
                    y = int(y / h) * h

                    if rook_white[i].selected:
                        if rook_white[i].x != x or rook_white[i].y != y:

                            rook_white[i].move(pygame.mouse.get_pos(), field, width, height)
                            deselectAll('white')



        drawBoard()
        for i in range(len(rook_black)):
            rook_black[i].show(screen, width, height)

        for i in range(len(rook_white)):
            rook_white[i].show(screen, width, height)
        pygame.display.update()
        clock.tick(15)

main()