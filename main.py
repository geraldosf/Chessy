import pygame
from objects.pieces import *
from function import *

pygame.init()
screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
running = True

tabletop = mount_tabletop()

movements = None
selected = None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:

            moved = False
            
            if selected:
                movements = calculate_moves(selected.piece, tabletop)
                for move in movements:
                    if tabletop[move[0]][move[1]].rect.collidepoint(pygame.mouse.get_pos()) == True:
                        move_piece(selected, tabletop[move[0]][move[1]])
                        selected = None
                        movements = None
                        moved = True
                        break
                
            if moved == False:
            
                for i in range(len(tabletop)):
                    for j in range(8):
                        if tabletop[i][j].rect.collidepoint(pygame.mouse.get_pos()) == True:
                            
                            if tabletop[i][j].piece != None:
                                selected = tabletop[i][j]
                                movements = calculate_moves(selected.piece, tabletop)


    screen.fill("black")

    for i in range(8):
        for j in range(8):
            if ((i + j) % 2 != 1):
                pygame.draw.rect(screen, "white", tabletop[i][j].rect)
                if tabletop[i][j].piece != None:
                    screen.blit(tabletop[i][j].piece.Image, tabletop[i][j].image_pos)
            else:
                pygame.draw.rect(screen, "brown", tabletop[i][j].rect)
                if tabletop[i][j].piece != None:
                    screen.blit(tabletop[i][j].piece.Image, tabletop[i][j].image_pos)
    
    if movements:
        for moves in movements:
            square = tabletop[moves[0]][moves[1]]
            pygame.draw.circle(screen, "blue", square.pos_center, 11)        

    pygame.display.flip()

    clock.tick(60)

pygame.quit()



