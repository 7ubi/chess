import pygame
import os
import chess_pieces

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("chess")



def drawBoard():
    for i in range(8):
        for j in range(8):
            if (j + i) % 2 == 0:
                pygame.draw.rect(screen, pygame.Color(102, 51, 0), (j * 100, i * 100, 100, 100))
            else:
                pygame.draw.rect(screen, pygame.Color(153, 102, 51), (j * 100, i * 100, 100, 100))



def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        drawBoard()
        pygame.display.update()

main()