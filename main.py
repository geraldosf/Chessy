import pygame
from chess_pos import chess_pos



def mount_table():
    table = [[], [], [], [], [], [], [], []]

    for i in range(8):
        for j in range(8):
            table[i].append(chess_pos((100 * (i + 1), 100 * (j + 1), 100, 100)))

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
            else:
                pygame.draw.rect(screen, "brown", table[i][j].rect)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()



