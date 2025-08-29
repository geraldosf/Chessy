import pygame
from objects.chess_pos import chess_pos
from objects.pieces import *



def mount_table():
    table = [[], [], [], [], [], [], [], []]

    for i in range(8):
        for j in range(8):
            pos = (100 * (i + 1), 100 * (j + 1))
            height = 100
            width = 100
            label = chr(97 + i) + str(8 - j)
            table[i].append(chess_pos(label, pos, height, width))

    return table



pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
running = True

table = mount_table()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for i in range(8):
        for j in range(8):
            if ((i + j) % 2 != 1):
                pygame.draw.rect(screen, "white", table[i][j].rect)
                if table[i][j].piece != None:
                    screen.blit(table[i][j].piece.Image, table[i][j].image_pos)
            else:
                pygame.draw.rect(screen, "brown", table[i][j].rect)
                if table[i][j].piece != None:
                    screen.blit(table[i][j].piece.Image, table[i][j].image_pos)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()



