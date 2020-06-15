import pygame
import os
import sys
from pieces import Rook
from pieces import Bishop

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess")

clock = pygame.time.Clock()

field = [[0 for x in range(8)] for y in range(8)]

rook_black = [Rook(1, 0, 0, width / 8, height / 8), Rook(1, 7 * width / 8, 0, width / 8, height / 8)]
rook_white = [Rook(-1, 0, 7 * height / 8, width / 8, height / 8), Rook(-1, 7 * width / 8, 7 * height / 8, width / 8, height / 8)]

bishop_black = [Bishop(1, 2 * width / 8, 0, width / 8, height / 8), Bishop(1, 5 * width / 8, 0, width / 8, height / 8)]
bishop_white = [Bishop(-1, 2 * width / 8, 7 * height / 8, width / 8, height / 8), Bishop(-1, 5 * width / 8, 7 * height / 8, width / 8, height / 8)]

turn = -1

def defPlayingField(): #black = 1 white = -1 nothing = 0
    global field
    field = [[0 for x in range(8)] for y in range(8)]

    for i in range(len(rook_black)):
        field[int(rook_black[i].x / width * 8)][int(rook_black[i].y / height * 8)] = 1

    for i in range(len(bishop_black)):
        field[int(bishop_black[i].x / width * 8)][int(bishop_black[i].y / height * 8)] = 1

    for i in range(len(rook_white)):
        field[int(rook_white[i].x / width * 8)][int(rook_white[i].y / height * 8)] = -1

    for i in range(len(bishop_white)):
        field[int(bishop_white[i].x / width * 8)][int(bishop_white[i].y / height * 8)] = -1

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

        for i in range(len(bishop_black)):
            bishop_black[i].setSelected(False)

    if c == 'white':
        for i in range(len(rook_white)):
            rook_white[i].setSelected(False)

        for i in range(len(bishop_white)):
            bishop_white[i].setSelected(False)

def takesBlack(x, y):
    for i in range(len(rook_black)):
        if int(x) == rook_black[i].x and int(y) == rook_black[i].y:
            rook_black.remove(rook_black[i])
            turn = 1
            return

    for i in range(len(bishop_black)):
        if int(x) == bishop_black[i].x and int(y) == bishop_black[i].y:
            bishop_black.remove(bishop_black[i])
            turn = 1
            return


def takesWhite(x, y):
    for i in range(len(rook_white)):
        if int(x) == rook_white[i].x and int(y) == rook_white[i].y:
            rook_white.remove(rook_white[i])
            turn = -1
            return

    for i in range(len(bishop_white)):
        if int(x) == bishop_white[i].x and int(y) == bishop_white[i].y:
            bishop_white.remove(bishop_white[i])
            turn = -1
            return

def movePiece(arr, colorNum, colorStr):
    for i in range(len(arr)):
        if arr[i].clickedOn(pygame.mouse.get_pos()):

            deselectAll(colorStr)
            arr[i].setSelected(True)

        x, y = pygame.mouse.get_pos()
        w, h = width/8, height/8
        x = int(x / w) * w
        y = int(y / h) * h

        if arr[i].selected:
            if arr[i].x != x or arr[i].y != y:

                if not arr[i].move(pygame.mouse.get_pos(), field, width, height):
                    continue

                i = int(x / width * 8)
                j = int(y / height * 8)

                if field[i][j] == -colorNum:
                    if colorNum == -1:
                        takesBlack(x, y)
                    else:
                        takesWhite(x, y)
                deselectAll(colorStr)
                return -colorNum
                
    return colorNum

def showPieces(arr):
    for i in range(len(arr)):
        arr[i].show(screen)

def main():
    turn = -1
    while True:
        defPlayingField()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                if turn == 1:
                    turn = movePiece(rook_black, 1, 'black')

                if turn == 1:
                    turn = movePiece(bishop_black, 1, 'black')

                if turn == -1:
                    turn = movePiece(rook_white, -1, 'white')

                if turn == -1:
                    turn = movePiece(bishop_white, -1, 'white')

        drawBoard()
        
        showPieces(rook_black)
        showPieces(rook_white)
        showPieces(bishop_black)
        showPieces(bishop_white)

        pygame.display.update()
        clock.tick(15)

main()