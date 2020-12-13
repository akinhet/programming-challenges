#!/usr/bin/python

import pygame

pygame.init()

wid = 600
hei = 600
ver_tiles = 30
hor_tiles = 30
ver_pixels = wid/hor_tiles
hor_pixels = hei/ver_tiles
vy = 0
vx = 0

screen = pygame.display.set_mode((wid, hei))


class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = hei/ver_tiles
        self.width = wid/hor_tiles
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 255, 255)

    def move(self, vx, vy):
        self.x += vx
        self.y += vy
        if self.x < 0 or self.x + self.width > wid or self.y < 0 or self.y + self.height > hei:
            self.x = wid/2
            self.y = hei/2
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.shape, 0)


player = Snake(wid/2, hei/2)

counter = 100

while True:
    screen.fill((0, 0, 0))
    player.draw()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                vy = -ver_pixels
                vx = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                vy = ver_pixels
                vx = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                vx = hor_pixels
                vy = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                vx = -hor_pixels
                vy = 0

    if counter < 1:
        player.move(vx, vy)
        counter = 100
    else:
        counter -= 1
