import pygame, sys, time, random
from pygame.locals import *
pygame.init()
black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colorList = [black, red, green, blue]
window = pygame.display.set_mode((400,600), 0, 32)
pygame.display.set_caption('ScreenSaver')

up = 'up'
down = 'down'
left = 'left'
right = 'right'

downLeft = 'downleft'
downRight = 'downright'
upLeft = 'upleft'
upRight = 'upright'
x = random.randint(0, 255)
y = random.randint(0, 255)
z = random.randint(0, 255)
# colors = random.choice(colorList)
movementSpeed = 4
Rectangle = {'rect':pygame.Rect(230, 120, 50, 50), 'color':(x, y, z), 'dir':downRight}
box = [Rectangle]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    window.fill(white)

    for b in box:
        if b['dir'] == downLeft:
            b['rect'].left -= movementSpeed
            b['rect'].top += movementSpeed
        if b['dir'] == downRight:
            b['rect'].left += movementSpeed
            b['rect'].top += movementSpeed
        if b['dir'] == upLeft:
            b['rect'].left -= movementSpeed
            b['rect'].top -= movementSpeed
        if b['dir'] == upRight:
            b['rect'].left += movementSpeed
            b['rect'].top -= movementSpeed
        if b['rect'].right > 400:
            b['color'] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            if b['dir'] == upRight:
                b['dir'] = downLeft
            if b['dir'] == downRight:
                b['dir'] = upLeft

        if b['rect'].bottom > 600:
            b['color'] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            if b['dir'] == downLeft:
                b['dir'] = upRight
            if b['dir'] == downRight:
                b['dir'] = upLeft

        if b['rect'].top < 0:
            b['color'] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            if b['dir'] == upLeft:
                b['dir'] = downLeft
            if b['dir'] == upRight:
                b['dir'] = downRight

        if b['rect'].left < 0:
            b['color'] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            if b['dir'] == downLeft:
                b['dir'] = downRight
            if b['dir'] == upLeft:
                b['dir'] = upRight
        if
        # qwer = '{}'
        # gj = qwer.format(player1Score)
        # qwrt = '{}'
        # gh = qwrt.format(player2Score)
        # text1 = basicFont.render(gj, True, white, black)
        # text2 = basicFont.render(gh, True, white, black)
        # text1Rect = text1.get_rect()
        # text2Rect = text2.get_rect()
        # text1Rect.centerx = windowSurface.get_rect().width - 50
        # text1Rect.centery = windowSurface.get_rect().height - 550
        # text2Rect.centerx = windowSurface.get_rect().width - 650
        # text2Rect.centery = windowSurface.get_rect().height - 550
        pygame.draw.rect(window, b['color'], b['rect'])

    pygame.display.update()
    time.sleep(1/30)
