from Chess import pieces
import pygame
from sys import exit


def main():
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    drawboard(screen)
    rook = pieces.Black_Rook(pygame.image.load('images/bR.png'),black)
    
    #events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        pygame.display.update()


def drawboard(screen):
    #white or black
    list_of_color = [(255,255,255), (105,105,105)]
    x_value, y_value = 0,0
    #by loop draw 64 rectangles alternating between white and black
    for vsquare in range (9):
        for hsquare in range (9):
            pygame.draw.rect(screen, list_of_color[(hsquare+vsquare)%2], pygame.Rect(x_value,y_value,50,50))
            x_value+=50
        x_value = 0
        y_value +=50

if __name__=="__main__":
    main()