#!/usr/bin/python

import pygame
import random

pygame.init()

wid = 600
hei = 600
ver_tiles = 30
hor_tiles = 30
ver_pixels = wid/hor_tiles
hor_pixels = hei/ver_tiles
vy = -ver_pixels
vx = 0

screen = pygame.display.set_mode((wid, hei))


class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = ver_pixels
        self.width = hor_pixels
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 255, 255)
        self.tail = []
        for i in range(5):
            self.tail.append(pygame.Rect(self.x, self.y+i*ver_pixels, self.width, self.height))

    def move(self, key):
        # Moving the tail
        tempx1 = self.x
        tempy1 = self.y
        tempx2 = 0
        tempy2 = 0
        for i in self.tail:
            tempx2 = i.x
            tempy2 = i.y
            i.x = tempx1
            i.y = tempy1
            tempx1 = tempx2
            tempy1 = tempy2

        if key == 'up':
            self.y -= ver_pixels
        elif key == 'down':
            self.y += ver_pixels
        elif key == 'right':
            self.x += hor_pixels
        elif key == 'left':
            self.x -= hor_pixels

        self.collision()

        if apple.is_eaten():
            self.tail.append(pygame.Rect(self.tail[-1].x, self.tail[-1].y, self.width, self.height))
        # Checking if the head hit the borders of the screen
        if self.x < 0 or self.x + self.width > wid or self.y < 0 or self.y + self.height > hei:
            self.respawn()

        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.shape, 0)
        for i in self.tail:
            pygame.draw.rect(screen, self.color, i, 0)

    def collision(self):
        for i in self.tail:
            if self.x == i.x and self.y == i.y:
                self.respawn()

    def respawn(self):
        self.x = wid/2
        self.y = hei/2
        self.tail = []
        for i in range(5):
            self.tail.append(pygame.Rect(self.x, self.y+i*ver_pixels, self.width, self.height))
        global prevkey
        prevkey = 'up'
        global currkey
        currkey = 'up'


class Apple():
    def __init__(self):
        self.x = random.randint(0, hor_tiles - 1) * hor_pixels
        self.y = random.randint(0, ver_tiles - 1) * ver_pixels
        while self.x == player.x and self.y == player.y:
            self.x = random.randint(0, hor_tiles - 1) * hor_pixels
            self.y = random.randint(0, ver_tiles - 1) * ver_pixels
        self.height = hor_pixels
        self.width = ver_pixels
        self.shape = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 0, 0)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.shape, 0)

    def is_eaten(self):
        if self.x == player.x and self.y == player.y:
            self.__init__()
            return True
        return False


player = Snake(wid/2, hei/2)

apple = Apple()

counter = 200
currkey = 'up'
prevkey = 'up'

while True:
    screen.fill((0, 0, 0))
    player.draw()
    apple.draw()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if prevkey != 'down':
                    currkey = 'up'
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if prevkey != 'up':
                    currkey = 'down'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if prevkey != 'left':
                    currkey = 'right'
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if prevkey != 'right':
                    currkey = 'left'

    if counter < 1:
        prevkey = currkey
        player.move(currkey)
        counter = 200
    else:
        counter -= 1
