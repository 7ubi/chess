import pygame
import os
import sys
from chess_pieces import Rook

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess")

clock = pygame.time.Clock()

def drawBoard():
    for i in range(8):
        for j in range(8):
            if (j + i) % 2 == 0:
                pygame.draw.rect(screen, pygame.Color(102, 51, 0), (int(j * width/8), int(i * height/8), int(width/8), int(height/8)))
            else:
                pygame.draw.rect(screen, pygame.Color(153, 102, 51), (int(j * width/8), int(i * height/8), int(width/8), int(height/8)))

rook1 = Rook('black', 0, 0, width/8, height/8)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if rook1.selected:
                    rook1.move(pygame.mouse.get_pos())

                if rook1.clickedOn(pygame.mouse.get_pos()):
                    rook1.setSelected(not rook1.selected)


        drawBoard()
        rook1.show(screen, width, height)
        pygame.display.update()
        clock.tick(15)

main()