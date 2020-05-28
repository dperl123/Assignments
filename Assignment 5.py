# Dylan Perlstein
# Assignment 5
# 5/27/20

import pygame, sys, time, random
from pygame.locals import *
from Assignment5Settings import *

# pygame window setup
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption(gameTitle)

# Player default movement setup
moveLeft = False
moveRight = False
jump = False

# Player setup
player = pygame.Rect(20, 230, 20, 40)
# Player position Y setup
posY = height - 20
basicFont = pygame.font.SysFont("Comic Sans MS", 20)
# Platform setup
platform0 = pygame.Rect(0, height - 20, width, platH)
platform1 = pygame.Rect(200, 200, 100, platH)
platform2 = pygame.Rect(350, 150, 50, platH)
platform3 = pygame.Rect(150, 230, 100, platH)
platform4 = pygame.Rect(0, 120, 100, platH)
platform5 = pygame.Rect(200, 60, 100, platH)
platform6 = pygame.Rect(300, 30, 100, platH)
platform7 = pygame.Rect(150, 55, 100, platH)
platformList = [platform0, platform1, platform2, platform3, platform4, platform5, platform6, platform7]
pygame.mixer.music.load('music/battleThemeA.mp3')
pygame.mixer.music.play(-1, 0)
pygame.mixer.music.set_volume(.2)
jumpSound = pygame.mixer.Sound('music/Various-06.wav')
landSound = pygame.mixer.Sound('music/Various-13.wav')
deadSentence = 'You Died! Click "R" to play again.'
deadText = basicFont.render(deadSentence, True, white)
# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
            if event.key == K_SPACE or event.key == K_w:
                jump = True
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_SPACE or event.key == K_w:
                jump = False
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(white)

    # Draw the platforms
    for platform in platformList:
        pygame.draw.rect(windowSurface, green, platform)

    # Gravity is always added to Y movement until it hits an object
    moveY += gravity

    # Set our movement when a direction is True
    if jump == True:
        # The player may only jump if they are touching a platform
        if player.collidelist(platformList) > -1:
            moveY = -10
            jumpSound.play()

    if player.x > width * 0.75:
        moveX -= 10
    score = 0
    if moveX < 0:
        for platform in platformList:
            platform.left = platform.left -8



    if moveLeft == True:
        player.left -= 4
        if player.left < 0:
            player.left = width
    if moveRight == True:
        player.right += 4
        if player.right > width:
            player.right = 0
    if player.left < 0:
        lives -=1
        player.x = 20
        player.y = 230
    # Y position of the player is updated with the Y movement
    posY += moveY + (.5 * gravity)
    player.bottom = posY

    # Checks for a collision with all platforms in the list and returns the index of the collision
    colliPos = player.collidelist(platformList)


    # if the player is falling, they can land on a platformPlatformer.py
    if moveY > 0:

        # if the player hits the side of a platform while falling, stop their horizontal movement by
        # keeping the player side and platform side the same.
        if moveRight and player.bottom > platformList[colliPos].centery:
            if colliPos > -1:
                jump = False
                moveRight = False
                if platformList[colliPos].left <= 0:
                    player.right = player.right
                else:
                    player.right = platformList[colliPos].left
        elif moveLeft and player.bottom > platformList[colliPos].centery:
            if colliPos > -1:
                jump = False
                moveLeft = False
                if platformList[colliPos].right >= width:
                    player.left = player.left
                else:
                    player.left = platformList[colliPos].right
        # if the index is greater that -1, the player must be touching ground, else, they are falling
        elif colliPos > -1:
            posY = platformList[colliPos].top + 1
            player.bottom = posY
            moveY = 0
    # if the player is jumping, they can't phase through the platform
    elif moveY < 0:
        if colliPos > -1:
            posY = platformList[colliPos].bottom + 40
            player.bottom = posY
            moveY += gravity
            jump = False

    # When the player reaches the top quarter of the screen, move the platforms down


    # remove platforms that fall off screen and add new ones to the top.
    for platform in platformList:
        if platform.left < 0:
            platWidth = random.choice(platW)
            platLeft = 380
            platTop = abs(random.randint(0, height - 20))
            platformList.append(pygame.Rect(platLeft, platTop, platWidth, platH))
            platformList.remove(platform)


    # If the player falls off screen, lose a life and place the player on lowest block
    if player.top >= height:
        posY = platformList[0].top
        player.centerx = platformList[0].centerx
        lives -= 1

    # Draw the player onto the surface.
    pygame.draw.rect(windowSurface, red, player)

    # when out of lives, game over
    if lives <= 0:
        windowSurface.fill(black)
        windowSurface.blit(deadText, (100, 100))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    lives = 3

    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)