import pygame
import os

pygame.init()

bishop_black = pygame.image.load(os.path.join('data', 'bishop_black.png')) 
bishop_white = pygame.image.load(os.path.join('data', 'bishop_white.png')) 

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

class Rook:
    def __init__(self, color):
        self.color = color
        