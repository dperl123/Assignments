# Assignment 3
# Dylan Perlstein
# 2/20/20
import pygame, sys, time, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()
white = (255, 255, 255)
pauseMusic = False
p = 2
bomb = pygame.image.load('images/bomb.jpg')
zombie = pygame.image.load('images/zombie.jpg')
play = pygame.image.load('images/start-button.jpg')
pause = pygame.image.load('images/pause.png')
stop = pygame.image.load('images/stop.jpg')
up = pygame.image.load('images/up.jpg')
down = pygame.image.load('images/down.png')
bombSound = pygame.mixer.Sound('music/bombSound.wav')
zombieSound = pygame.mixer.Sound('music/Enraged_Zombies-Mike_Koenig-541225828.wav')
pygame.mixer.music.load('music/battleThemeA.mp3')
pygame.mixer.music.play(-1, 0)
pygame.mixer.music.set_volume(.2)
x = 80
y = 80
q = 20
r = 20
z = .2
playerZombie = pygame.Rect(100, 300, x, y)
playerBomb = pygame.Rect(700, 200, x, y)
playerPlay = pygame.Rect(780, 0, q, r)
playerPause = pygame.Rect(780, 20, q, r)
playerStop = pygame.Rect(780, 40, q, r)
playerUp = pygame.Rect(780, 60, q, r)
playerDown = pygame.Rect(780, 80, q, r)

window = pygame.display.set_mode((800, 400), 0, 32)
pygame.display.set_caption('Assignment 3')

while True:
    window.fill(white)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if 100 < event.pos[0] < 180 and 300 < event.pos[1] < 380:
                    zombieSound.play()
                    zombie = pygame.transform.rotate(zombie, 90)
                if 700 < event.pos[0] < 780 and 200 < event.pos[1] < 280:
                    bombSound.play()
                    bomb = pygame.transform.rotate(bomb, -90)
                if 780 < event.pos[0] < 800:
                    if 0 < event.pos[1] < 20:
                        pygame.mixer.music.play(-1, 0)
                    if 20 < event.pos[1] < 30:
                        pygame.mixer.music.pause()
                    if 30 < event.pos[1] < 40:
                        pygame.mixer.music.unpause()
                    if 40 < event.pos[1] < 60:
                        pygame.mixer.music.stop()
                    if 60 < event.pos[1] < 80:
                        pygame.mixer.music.set_volume(z + .2)
                        z += .2
                    if 80 < event.pos[1] < 100:
                        pygame.mixer.music.set_volume(z - .2)
                        z -= .2
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                if pauseMusic == False:
                    pauseMusic = True
                if pauseMusic == True:
                    pauseMusic = False
    window.fill(white)
    zombieStretch = pygame.transform.scale(zombie, (x, y))
    bombStretch = pygame.transform.scale(bomb, (x, y))
    playStretch = pygame.transform.scale(play, (q, r))
    pauseStretch = pygame.transform.scale(pause, (q, r))
    stopStretch = pygame.transform.scale(stop, (q, r))
    upStretch = pygame.transform.scale(up, (q, r))
    downStretch = pygame.transform.scale(down, (q, r))
    window.blit(zombieStretch, playerZombie)
    window.blit(bombStretch, playerBomb)
    window.blit(playStretch, playerPlay)
    window.blit(pauseStretch, playerPause)
    window.blit(stopStretch, playerStop)
    window.blit(upStretch, playerUp)
    window.blit(downStretch, playerDown)
    pygame.display.update()
    mainClock.tick(60)
