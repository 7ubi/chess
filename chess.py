import pygame
import os
import sys
from pieces import Rook
from pieces import Bishop
from pieces import King
from pieces import Queen
from pieces import Knight
from pieces import Pawn
import math
import copy

pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess")

clock = pygame.time.Clock()

field = [[0 for x in range(8)] for y in range(8)]

blackpieces = []
blackpieces.append(Rook(1, 0, 0, width / 8, height / 8, 50))
blackpieces.append(Rook(1, 7 * width / 8, 0, width / 8, height / 8, 50))
blackpieces.append(Bishop(1, 2 * width / 8, 0, width / 8, height / 8, 30))
blackpieces.append(Bishop(1, 5 * width / 8, 0, width / 8, height / 8, 30))
blackpieces.append(King(1, 4 * width / 8, 0, width / 8, height / 8, 900))
blackpieces.append(Queen(1, 3 * width / 8, 0, width / 8, height / 8, 90))
blackpieces.append(Knight(1, width / 8, 0, width / 8, height / 8, 30))
blackpieces.append(Knight(1, 6 * width / 8, 0, width / 8, height / 8, 30))

for i in range(8):
    blackpieces.append(Pawn(1, i * width / 8, height / 8, width / 8, height / 8, 10))

whitepieces = []
whitepieces.append(Rook(-1, 0, 7 * height / 8, width / 8, height / 8, -50))
whitepieces.append(Rook(-1, 7 * width / 8, 7 * height / 8, width / 8, height / 8, -50))
whitepieces.append(Bishop(-1, 2 * width / 8, 7 * height / 8, width / 8, height / 8, -30))
whitepieces.append(Bishop(-1, 5 * width / 8, 7 * height / 8, width / 8, height / 8, -30))
whitepieces.append(King(-1, 4 * width / 8, 7 * height / 8, width / 8, height / 8, -900))
whitepieces.append(Queen(-1, 3 * width / 8, 7 * height / 8, width / 8, height / 8, -90))
whitepieces.append(Knight(-1, width / 8, 7 * height / 8, width / 8, height / 8, -30))
whitepieces.append(Knight(-1, 6 * width / 8, 7 * height / 8, width / 8, height / 8, -30))

for i in range(8):
    whitepieces.append(Pawn(-1, i * width / 8, 6 * height / 8, width / 8, height / 8, -10))

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
    print("nice")
    for i in range(len(blackpieces)):
        if int(x) == blackpieces[i].x and int(y) == blackpieces[i].y:
            blackpieces.remove(blackpieces[i])
            turn = 1
            return


def takesWhite(x, y):
    # print(len(whitepieces))
    for i in range(len(whitepieces)):
        print(whitepieces[i].x, x, whitepieces[i].y, y, i)
        if int(x) == int(whitepieces[i].x) and int(y) == int(whitepieces[i].y):
            print("hey")
            whitepieces.remove(whitepieces[i])
            turn = -1
            return

def movePiece(arr, colorNum, colorStr, pos):
    x, y = pos
    for i in range(len(arr)):
        if arr[i].clickedOn(pygame.mouse.get_pos()):

            deselectAll(colorStr)
            arr[i].setSelected(True)

        
        w, h = width/8, height/8
        x = int(x / w) * w
        y = int(y / h) * h
        # print(x, y, arr[i].selected)
        if arr[i].selected:
            if arr[i].x != x or arr[i].y != y:

                if not arr[i].move((x, y), field, width, height):
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
        arr[i].showAllMoves(field, screen)

def getScore():
    score = 0
    for i in range(len(blackpieces)):
        score += blackpieces[i].score

    for i in range(len(whitepieces)):
        score += whitepieces[i].score
    # print(len(blackpieces), len(whitepieces))
    if score != 0:
        print(score)
    return score

def AIMove(depth):
    index = 0
    moveX = 0
    moveY = 0


    m = -math.inf
    for i in range(len(blackpieces)):
        
        blackpieces[i].getAllMoves(field)
        x = blackpieces[i].x
        y = blackpieces[i].y
        for move in range(len(blackpieces[i].allMoves)):
            temp = []
            for j in range(len(whitepieces)):
                temp.append(whitepieces[j])

            blackpieces[i].makeAllMoves(move, field)
            score = minimaxi(depth - 1, False)
            whitepieces.clear()
            for j in range(len(temp)):
                whitepieces.append(temp[j])
            if score > m:
                m = score
                index = i
                moveX = blackpieces[i].x
                moveY = blackpieces[i].y

        blackpieces[i].x = x
        blackpieces[i].y = y
    blackpieces[index].selected = True
    # print(moveX, moveY)
    movePiece(blackpieces, 1, 'black', (moveX, moveY))

def minimaxi(depth, maxi): #black
    if depth == 0:
        # print("hey", depth, maxi)
        return getScore()
    # print(depth, maxi)
    m = 0
    if maxi:
        m = -10000

        for i in range(len(blackpieces)):
            
            blackpieces[i].getAllMoves(field)
            x = blackpieces[i].x
            y = blackpieces[i].y
            for move in range(len(blackpieces[i].allMoves)):
                temp = []
                for j in range(len(whitepieces)):
                    temp.append(whitepieces[j])
                blackpieces[i].makeAllMoves(move, field)
                score = minimaxi(depth - 1, False)
                whitepieces.clear()
                for j in range(len(temp)):
                    whitepieces.append(temp[j])
                if score > m:
                    m = score

            blackpieces[i].x = x
            blackpieces[i].y = y
    else:
        m = 10000
        # print(len(whitepieces))
        for i in range(len(whitepieces)):
            if i > len(whitepieces):
                break
            whitepieces[i].getAllMoves(field)
            x = whitepieces[i].x
            y = whitepieces[i].y

            for move in range(len(whitepieces[i].allMoves)):
                whitepieces[i].makeAllMoves(move, field)
                temp = []

                for j in range(len(blackpieces)):
                    temp.append(blackpieces[j])

                score = minimaxi(depth - 1, True)
                
                if score < m:
                    m = score
                blackpieces.clear()
                for j in range(len(temp)):
                    blackpieces.append(temp[j])
            whitepieces[i].x = x
            whitepieces[i].y = y
    return m


def main():
    turn = -1
    while True:
        defPlayingField()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                # if turn == 1:
                #     turn = movePiece(blackpieces, 1, 'black')

                if turn == -1:
                    turn = movePiece(whitepieces, -1, 'white', pygame.mouse.get_pos())

        drawBoard()
        
        if turn == 1:
            # print("hey")
            AIMove(3)
            turn = -1


        showPieces(blackpieces)
        showPieces(whitepieces)
        
        pygame.display.update()
        clock.tick(15)
if __name__ == "__main__":
    main()
