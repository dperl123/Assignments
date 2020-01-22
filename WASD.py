import pygame, sys, time, random
from pygame.locals import *
pygame.init()
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colorList = [black, red, green, blue]
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
movementSpeed = 3
window = pygame.display.set_mode((500,500), 0, 32)
pygame.display.set_caption('WASD')
player = [250, 250]
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    window.fill(white)
    if event.type == KEYDOWN:
        if event.key == K_UP or event.key == K_w:
            moveUp = True
        if event.key == K_DOWN or event.key == K_s:
            moveDown = True
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = True
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = True
    if event.type == KEYUP:
        if event.key == K_UP or event.key == K_w:
            moveUp = False
        if event.key == K_DOWN or event.key == K_s:
            moveDown = False
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = False
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = False
    if moveUp == True:
        player[1] -= movementSpeed
        if player[1] < 0:
            player[1] = 500
    if moveDown == True:
        player[1] += movementSpeed
        if player[1] > 500:
            player[1] = 0
    if moveLeft == True:
        player[0] -= movementSpeed
        if player[0] < 0:
            player[0] = 500
    if moveRight == True:
        player[0] += movementSpeed
        if player[0] > 500:
            player[0] = 0
    pygame.draw.circle(window, green, player, 30)
    pygame.display.update()
    time.sleep(1/60)