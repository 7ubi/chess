import pygame
import os
import sys
from pieces import Rook
from pieces import Bishop
from pieces import King
from pieces import Queen
from pieces import Knight
from pieces import Pawn

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess")

clock = pygame.time.Clock()

field = [[0 for x in range(8)] for y in range(8)]

blackpieces = []
blackpieces.append(Rook(1, 0, 0, width / 8, height / 8))
blackpieces.append(Rook(1, 7 * width / 8, 0, width / 8, height / 8))
blackpieces.append(Bishop(1, 2 * width / 8, 0, width / 8, height / 8))
blackpieces.append(Bishop(1, 5 * width / 8, 0, width / 8, height / 8))
blackpieces.append(King(1, 4 * width / 8, 0, width / 8, height / 8))
blackpieces.append(Queen(1, 3 * width / 8, 0, width / 8, height / 8))
blackpieces.append(Knight(1, width / 8, 0, width / 8, height / 8))
blackpieces.append(Knight(1, 6 * width / 8, 0, width / 8, height / 8))

for i in range(8):
    blackpieces.append(Pawn(1, i * width / 8, height / 8, width / 8, height / 8))

whitepieces = []
whitepieces.append(Rook(-1, 0, 7 * height / 8, width / 8, height / 8))
whitepieces.append(Rook(-1, 7 * width / 8, 7 * height / 8, width / 8, height / 8))
whitepieces.append(Bishop(-1, 2 * width / 8, 7 * height / 8, width / 8, height / 8))
whitepieces.append(Bishop(-1, 5 * width / 8, 7 * height / 8, width / 8, height / 8))
whitepieces.append(King(-1, 4 * width / 8, 7 * height / 8, width / 8, height / 8))
whitepieces.append(Queen(-1, 3 * width / 8, 7 * height / 8, width / 8, height / 8))
whitepieces.append(Knight(-1, width / 8, 7 * height / 8, width / 8, height / 8))
whitepieces.append(Knight(-1, 6 * width / 8, 7 * height / 8, width / 8, height / 8))

for i in range(8):
    whitepieces.append(Pawn(-1, i * width / 8, 6 * height / 8, width / 8, height / 8))

turn = -1

def defPlayingField(): #black = 1 white = -1 nothing = 0
    global field
    field = [[0 for x in range(8)] for y in range(8)]

    for i in range(len(blackpieces)):
        field[int(blackpieces[i].x / width * 8)][int(blackpieces[i].y / height * 8)] = 1

    for i in range(len(whitepieces)):
        field[int(whitepieces[i].x / width * 8)][int(whitepieces[i].y / height * 8)] = -1


def drawBoard():
    for i in range(8):
        for j in range(8):
            if (j + i) % 2 == 0:
                pygame.draw.rect(screen, pygame.Color(102, 51, 0), (int(j * width/8), int(i * height/8), int(width/8), int(height/8)))
            else:
                pygame.draw.rect(screen, pygame.Color(153, 102, 51), (int(j * width/8), int(i * height/8), int(width/8), int(height/8)))

def deselectAll(c):
    if c == 'black':
        for i in range(len(blackpieces)):
            blackpieces[i].setSelected(False)

    if c == 'white':
        for i in range(len(whitepieces)):
            whitepieces[i].setSelected(False)


def takesBlack(x, y):
    for i in range(len(blackpieces)):
        if int(x) == blackpieces[i].x and int(y) == blackpieces[i].y:
            blackpieces.remove(blackpieces[i])
            turn = 1
            return


def takesWhite(x, y):
    for i in range(len(whitepieces)):
        if int(x) == whitepieces[i].x and int(y) == whitepieces[i].y:
            whitepieces.remove(whitepieces[i])
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
                    turn = movePiece(blackpieces, 1, 'black')

                if turn == -1:
                    turn = movePiece(whitepieces, -1, 'white')

        drawBoard()
        
        showPieces(blackpieces)
        showPieces(whitepieces)

        pygame.display.update()
        clock.tick(15)

main()