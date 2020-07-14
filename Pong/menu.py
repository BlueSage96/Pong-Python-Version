import pygame
import sys
import pygame.gfxdraw, pygame.font
from enum import Enum

#background image - last image:
#https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame#28005796

#buttons
#https://pythonprogramming.net/pygame-button-function/

#button outline thickness:
#https://www.youtube.com/watch?v=4_9twnEduFA

#importing other methods
#https://www.youtube.com/watch?v=P6sdJsSOIG8

pygame.init()
screen = pygame.display.set_mode((960,640))
pygame.display.set_caption('Pong')
background = pygame.image.load("Atari.jpg")
sys.setrecursionlimit(10000) # 10000 is an example, try with different values
white = (255, 255, 255)
black = (0, 0, 0)

blue = (0,0,200)
red = (200,0,0)
green = (0,200,0)

bright_blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)

class GameState(Enum):
    PAUSED = -2
    QUIT = -1
    TITLE = 0
    STARTGAME = 1
    MENU = 2

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, action=None, outline=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if outline:
        # *2 affects outline thickness
        pygame.draw.rect(screen,outline, (x-2*2, y-2*2, w+4*2, h+4*2), 0)
    # print(click)
    game_state = GameState.TITLE
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            #play doesn't work
            if action == "play":
                game_state = GameState.STARTGAME

            elif action == "exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("Arial",60)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)

def start_menu():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))
        button("Start",380,200,200,60,green,bright_green, "play", black)
        button("Quit",380, 400, 200, 60, red, bright_red, "exit", black)

        pygame.display.update()
start_menu()
