# Pong
# Dylan Perlstein
# 1/29/2020
import pygame, sys, time, random
from pygame.locals import *

# Set up pygame. to run pygame, we must always initialize it.
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
moveUp = False
moveDown = False
moveDown2 = False
moveUp2 = False
movementSpeed = 12
ballSpeed = 8
player1Score = 0
player2Score = 0
player1Games = 0
player2Games = 0
basicFont = pygame.font.SysFont("Comic Sans MS", 50)
# Here we create the window. We store the window height and width in variables so we can use them later.
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


width = 700
height = 600
list = [upRight, upLeft, downRight, downLeft]
list1 = [upRight, downRight]
list2 = [upLeft, downLeft]
direction = random.choice(list)
windowSurface = pygame.display.set_mode((width, height), 0, 32)


rect1 = {'rect':pygame.Rect(685, 270, 15, 60), 'color': white, 'dir': up}
rect2 = {'rect':pygame.Rect(0, 270, 15, 60), 'color': red, 'dir': up}

player1 = pygame.Rect(685, 270, 15, 60)
player2 = pygame.Rect(0, 270, 15, 60)


ball = {'rect':pygame.Rect(350,300, 10, 10), 'color': red, 'dir': direction}

balls = pygame.Rect(350, 300, 10, 10)
box = [ball]
rectangle = [rect1, rect2]
# Set the window title to "Pong"
pygame.display.set_caption('Pong')








# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(black)
    player1TextScore = '{}'
    player1Sentence = player1TextScore.format(player1Score)
    player2TextScore = '{}'
    player2Sentence = player2TextScore.format(player2Score)
    player1GameScore = '{}'
    player1GameScoreSentence = player1GameScore.format(player1Games)
    player2GameScore = '{}'
    player2GameScoreSentence = player2GameScore.format(player2Games)
    text1 = basicFont.render(player1Sentence, True, white, black)
    text2 = basicFont.render(player2Sentence, True, white, black)
    text3 = basicFont.render(player1GameScoreSentence, True, white, black)
    text4 = basicFont.render(player2GameScoreSentence, True, white, black)
    winText = 'Woohoo, you have won the match!'
    win = basicFont.render(winText, True, white, black)
    text1Rect = text1.get_rect()
    text2Rect = text2.get_rect()
    text3Rect = text3.get_rect()
    text4Rect = text4.get_rect()
    winRect = win.get_rect()
    text1Rect.centerx = windowSurface.get_rect().width - 50
    text1Rect.centery = windowSurface.get_rect().height - 550
    text2Rect.centerx = windowSurface.get_rect().width - 650
    text2Rect.centery = windowSurface.get_rect().height - 550
    winRect.centerx = windowSurface.get_rect().centerx
    winRect.centery = windowSurface.get_rect().centery
    text3Rect.centerx = windowSurface.get_rect().centerx + 40
    text3Rect.centery = windowSurface.get_rect().height - 550
    text4Rect.centerx = windowSurface.get_rect().centerx - 40
    text4Rect.centery = windowSurface.get_rect().height - 550


    if event.type == KEYDOWN:
        if event.key == K_UP:
            moveUp = True
        if event.key == K_DOWN:
            moveDown = True
        if event.key == K_w:
            moveUp2 = True
        if event.key == K_s:
            moveDown2 = True

    if moveUp == True:
        player1[1] -= movementSpeed
        rect1['color'] = (random.randint(20,255), random.randint(20,255), random.randint(20,255))
    if moveDown == True:
        player1[1] += movementSpeed
        rect1['color'] = (random.randint(20,255), random.randint(20,255), random.randint(20,255))
    if moveUp2 == True:
        player2[1] -= movementSpeed
        rect2['color'] = (random.randint(20,255), random.randint(20,255), random.randint(20,255))
    if moveDown2 == True:
        player2[1] += movementSpeed
        rect2['color'] = (random.randint(20,255), random.randint(20,255), random.randint(20,255))





    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.key == K_UP:
            moveUp = False
        if event.key == K_DOWN:
            moveDown = False
        if event.key == K_w:
            moveUp2 = False
        if event.key == K_s:
            moveDown2 = False

    for b in box:
        if b['dir'] == downLeft:
            b['rect'].left -= ballSpeed
            b['rect'].top += ballSpeed
        if b['dir'] == downRight:
            b['rect'].left += ballSpeed
            b['rect'].top += ballSpeed
        if b['dir'] == upLeft:
            b['rect'].left -= ballSpeed
            b['rect'].top -= ballSpeed
        if b['dir'] == upRight:
            b['rect'].left += ballSpeed
            b['rect'].top -= ballSpeed
        if b['rect'].bottom > 600:
            b['color'] = (random.randint(20,255), random.randint(20,255), random.randint(20,255))
            if b['dir'] == downLeft:
                b['dir'] = upLeft
            if b['dir'] == downRight:
                b['dir'] = upRight
        if b['rect'].top < 0:
            b['color'] = (random.randint(20,255), random.randint(20,255), random.randint(20,255))
            if b['dir'] == upLeft:
                b['dir'] = downLeft
            if b['dir'] == upRight:
                b['dir'] = downRight
        if b['rect'].colliderect(player1):
            if b['dir'] == upRight:
                b['dir'] = random.choice(list2)
            if b['dir'] == downRight:
                b['dir'] = random.choice(list2)
        if b['rect'].colliderect(player2):
            if b['dir'] == upLeft:
                b['dir'] = random.choice(list1)
            if b['dir'] == downLeft:
                b['dir'] = random.choice(list1)
        if b['rect'].left < -20:
            player1Score += 1
            if player1Score > 7:
                player1Games += 1
                if player1Games >= 3:
                    windowSurface.fill(black)
                    windowSurface.blit(win, winRect)
                player1Score = 0
                player2Score = 0
            player1[1] = 300
            player2[1] = 300
            time.sleep(1.5)
            b['rect'].x = 350
            b['rect'].y = 300
            if b['dir'] == upRight:
                b['dir'] == random.choice(list)
            if b['dir'] == upLeft:
                b['dir'] == random.choice(list)
            if b['dir'] == downRight:
                b['dir'] == random.choice(list)
            if b['dir'] == downLeft:
                b['dir'] = random.choice(list)
        if b['rect'].right > 720:
            player2Score += 1
            if player2Score > 7:
                player2Games += 1
                player1Score = 0
                player2Score = 0
            player1[1] = 300
            player2[1] = 300
            time.sleep(1.5)
            b['rect'].x = 350
            b['rect'].y = 300
            if b['dir'] == upRight:
                b['dir'] == random.choice(list)
            if b['dir'] == upLeft:
                b['dir'] == random.choice(list)
            if b['dir'] == downRight:
                b['dir'] == random.choice(list)
            if b['dir'] == downLeft:
                b['dir'] = random.choice(list)
    pygame.draw.line(windowSurface, white, (350, 0), (350, 600), 5)
    windowSurface.blit(text1, text1Rect)
    windowSurface.blit(text2, text2Rect)
    windowSurface.blit(text3, text3Rect)
    windowSurface.blit(text4, text4Rect)
    pygame.draw.rect(windowSurface, b['color'], b['rect'])
    pygame.draw.rect(windowSurface, (random.randint(20,255), random.randint(20,255), random.randint(20,255)), player1)
    pygame.draw.rect(windowSurface, (random.randint(20,255), random.randint(20,255), random.randint(20,255)), player2)
    if player1Games >= 3:
        windowSurface.fill(black)
        windowSurface.blit(win, winRect)
    if player2Games >= 3:
        windowSurface.fill(black)
        windowSurface.blit(win, winRect)



    # Draw the window onto the screen.
    pygame.display.update()

    # Set the framerate of the game.
    mainClock.tick(30)

# Paragraph on Pong
# Pong is a game because there are two players controlling different paddles with a goal of not allowing a ball to go by them.
# It is competitive, takes a certain level of skill/ hand eye coordination, and has an objective for the players. The user
# experience is one that allows the player to compete against a friend or the computer to try and block the ball from going past
# the edge of the screen with a paddle. It is fun because it does not take a whole lot of skill, but still allows for some friendly
# competition. If I were to improve the game, I would make it much more colorful and add some music to it to make the game more lively
# and interesting.
