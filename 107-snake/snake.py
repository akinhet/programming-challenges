import pygame

pygame.init()

wid = 600
hei = 600
pixel = 6

screen = pygame.display.set_mode((wid,hei))

class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y

