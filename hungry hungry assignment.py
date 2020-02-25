# Hungry Hungry Assignment 2
# Dylan Perlstein
# 2/6/20
import  pygame, sys, time, random
from pygame.locals import *
pygame.init()
mainClock = pygame.time.Clock()
up = 'up'
down = 'down'
left = 'left'
right = 'right'
downLeft = 'downleft'
downRight = 'downright'
upLeft = 'upleft'
upRight = 'upright'
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
grow = False
shrink = False
angle = 0
left = False
right = False
up = True
down = False
basicFont = pygame.font.SysFont("Comic Sans MS", 20)
movementSpeed = 5
score = 0
scoreText = 'You have {} points'
scoreSentence = scoreText.format(score)



black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
x = 50
y = 100
x1 = 40
y1 = 40
text1 = basicFont.render(scoreSentence, True, black)
player = pygame.Rect(400 - 25 , 400 - 50, x, y)
playerImage = pygame.image.load('po the panda.jpg')

food = pygame.Rect(random.randint(40,760), random.randint(40,760), x1, y1)

foodImage = pygame.image.load('dumplings.jpg')
width = 800
height = 800
windowSurface = pygame.display.set_mode((width, height), 0, 32)
windowSurface.fill(white)
pygame.display.set_caption('Hungry Hungry Pygame')

while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == KEYDOWN:
        if event.key == K_UP or event.key == K_w:
            moveUp = True
        if event.key == K_DOWN or event.key == K_s:
            moveDown = True
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = True
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = True
        if event.key == K_SPACE:
            grow = True
        if event.key == K_z:
            shrink = True
    if event.type == KEYUP:
        if event.key == K_UP or event.key == K_w:
            moveUp = False
        if event.key == K_DOWN or event.key == K_s:
            moveDown = False
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = False
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = False
        if event.key == K_SPACE:
            grow = False
        if event.key == K_z:
            shrink = False
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if moveUp == True:
            player.top -= movementSpeed
            if left == True:
                playerImage = pygame.transform.rotate(playerImage, -90)
                left = False
            if right == True:
                playerImage = pygame.transform.rotate(playerImage, 90)
                right = False
            if down == True:
                playerImage = pygame.transform.flip(playerImage, False, True)
                down = False
            up = True

        if moveDown == True:
            player.top += movementSpeed
            if left == True:
                playerImage = pygame.transform.rotate(playerImage, 90)
                left = False
            if right == True:
                playerImage = pygame.transform.rotate(playerImage, -90)
                right = False
            if up == True:
                playerImage = pygame.transform.flip(playerImage, False, True)
                up = False
            down = True

        if moveLeft == True:
            player.left -= movementSpeed
            if right == True:
                playerImage = pygame.transform.rotate(playerImage, 180)
                right = False
            if up == True:
                playerImage = pygame.transform.rotate(playerImage, 90)
                up = False
            if down == True:
                playerImage = pygame.transform.rotate(playerImage, -90)
                down = False
            left = True

        if moveRight == True:
            player.right += movementSpeed
            if left == True:
                playerImage = pygame.transform.rotate(playerImage, 180)
                left = False
            if up == True:
                playerImage = pygame.transform.rotate(playerImage, -90)
                up = False
            if down == True:
                playerImage = pygame.transform.rotate(playerImage, 90)
                down = False
            right = True

            if player.colliderect(food):
                score += 1
                food.x = random.randint(40,760)
                food.y = random.randint(40,760)
                scoreText = 'You have {} points'
                scoreSentence = scoreText.format(score)
                text1 = basicFont.render(scoreSentence, True, black)

        windowSurface.fill(white)
        playerImageStretch = pygame.transform.scale(playerImage, (x, y))
        foodImageStretch = pygame.transform.scale(foodImage,(x1, y1))
        windowSurface.blit(text1, (400, 20))
        windowSurface.blit(playerImageStretch, player)
        windowSurface.blit(foodImageStretch, food)


        # windowSurface.blit(score, windowSurface.get_rect().centerx, windowSurface.get_rect().centery - 390)
        pygame.display.update()
        mainClock.tick(60)

