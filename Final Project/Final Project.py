import pygame, sys, random
from pygame.locals import *
from PlatformerSettings import *

# pygame window setup
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption(gameTitle)

# Player default movement setup
moveLeft = False
moveRight = False
moveUp = False
jump = True
monsterSpeed = 2

# Player setup
player = pygame.Rect(width/2-20, 160, 20, 40)
# Player position Y setup
posY = height - 20
basicFont = pygame.font.SysFont("Comic Sans MS", 20)

# Platform setup
platform0 = pygame.Rect(0, height - 20, width, platH)
platform1 = pygame.Rect(200, 400, 100, platH)
platform2 = pygame.Rect(350, 325, 50, platH)
platform3 = pygame.Rect(240, 250, 100, platH)
platform4 = pygame.Rect(150, 200, 100, platH)
platform5 = pygame.Rect(225, 115, 100, platH)
platform6 = pygame.Rect(10, 85, 100, platH)
platform7 = pygame.Rect(150, 5, 100, platH)
platformList = [platform0, platform1, platform2, platform3, platform4, platform5, platform6, platform7]
colorList = [green, red, blue, black, yellow]
SpringXCoord = [230, 380, 180, 30, 180, 330, 105]
SpringYCoord = [370, 295, 220, 170, 70, 40]
score = 0
flame = pygame.image.load('images/flame.jpg')
flamePlayer = pygame.Rect(255, 85, 30, 30)
monster1 = pygame.image.load('images/monster1.jpg')
monster1Player = pygame.Rect(340, 120, 60, 60)
monster2 = pygame.image.load('images/monster2.png')
monster2Player = pygame.Rect(80, 65, 40, 40)
deadSentence = 'You Died! Click "R" to play again.'
deadText = basicFont.render(deadSentence, True, white)
pygame.mixer.music.load('music/battleThemeA.mp3')
pygame.mixer.music.play(-1, 0)
pygame.mixer.music.set_volume(.2)
deathSound = pygame.mixer.Sound('music/bombSound.wav')

# monsterList = [monster1Player]
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
            # if event.key == K_SPACE or event.key == K_w:
            #     jump = True
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            # if event.key == K_SPACE or event.key == K_w:
            #     jump = False
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(white)
    monster1Player.y += monsterSpeed
    if monster1Player.y >= height:
        monster1Player.y = 0
    monster2Player.y -= monsterSpeed
    if monster2Player.y <= 0:
        monster2Player.y = height
    flamePlayer.x += random.randint(-8, 8)
    flamePlayer.y += random.randint(-8, 8)
    if flamePlayer.x >= width:
        flamePlayer.x = 200
    if flamePlayer.x <= 0:
        flamePlayer.x = 200
    if flamePlayer.y >= height:
        flamePlayer.y = 250
    if flamePlayer.y <= 0:
        flamePlayer.y = 250
    # Draw the platforms
    for platform in platformList:
        pygame.draw.rect(windowSurface, green, platform)

    # Gravity is always added to Y movement until it hits an object
    moveY += gravity

    # Set our movement when a direction is True
    if jump == True:
        # The player may only jump if they are touching a platform
        if player.collidelist(platformList) > -1:
            score += 100
            moveY = -10
        if player.colliderect(flamePlayer):
            moveUp = True
            moveY = -17
            flamePlayer.y -= 30
        if player.colliderect(monster1Player):
            lives -= 1
            deathSound.play()
        if player.colliderect(monster2Player):
            lives -= 1
            deathSound.play()


    if moveLeft == True:
        player.left -= moveX
        if player.left < 0:
            player.left = width
    if moveRight == True:
        player.right += moveX
        if player.right > width:
            player.right = 0

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
                jump = True
                moveRight = False
                if platformList[colliPos].left <= 0:
                    player.right = player.right
                else:
                    player.right = platformList[colliPos].left
        elif moveLeft and player.bottom > platformList[colliPos].centery:
            if colliPos > -1:
                jump = True
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
            jump = True

    # When the player reaches the top quarter of the screen, move the platforms down
    if player.bottom <= height/4:
        for platform in platformList:
            platform.top = platform.top + 8

    # remove platforms that fall off screen and add new ones to the top.
    for platform in platformList:
        x = 0
        if platform.top > height:
            platWidth = 80
            platLeft = x + random.randint(player.x - 100, player.x + 100)
            platTop = -20
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
        flamePlayer.x = 1200
        monster2Player.x = 2000
        monster1Player.x = 3000
        windowSurface.blit(deadText, (100, 250))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    lives = 1

    FlameImageStretch = pygame.transform.scale(flame, (30, 30))
    monster1ImageStretch = pygame.transform.scale(monster1, (60, 60))
    monster2ImageStretch = pygame.transform.scale(monster2, (40, 40))
    windowSurface.blit(FlameImageStretch, flamePlayer)
    windowSurface.blit(monster1ImageStretch, monster1Player)
    windowSurface.blit(monster2ImageStretch, monster2Player)
    # Draw the window onto the screen.
    pygame.display.update()
    # Set the framerate of the game.
    mainClock.tick(60)