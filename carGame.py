import pygame
import sys
import time
import random
import math

pygame.init()  # initializes the Pygame

screen = pygame.display.set_mode((798, 600))

# changing title of the game window
pygame.display.set_caption('Racing Car')

# changing the logo
logo = pygame.image.load('car game/logo.jpg')
pygame.display.set_icon(logo)

# color
red = (255, 0, 0)
blue = (0,0,255)


def gameOver():
    pygame.mixer.music.stop()
    gFont = pygame.font.SysFont('Arial Black', 100)
    GOsurf = gFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (400, 50)
    screen.blit(GOsurf, GOrect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()  # pygame exit
    sys.exit()

def restart():
    RFont = pygame.font.SysFont('Arial Black',50)
    GOsurf = RFont.render('Restart', True, blue)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (400, 50)
    screen.blit(GOsurf, GOrect)
    pygame.display.flip()
    gameloop()

def count():
    logo = pygame.image.load('car game/logo.jpg')

    for i in range(3, 0, -1):
        green = (0, 255, 0)
        screen.blit(logo, (200, 80))
        sc = str(i)
        gFont = pygame.font.SysFont('Arial Black', 100)
        GOsurf = gFont.render(sc, True, green)
        GOrect = GOsurf.get_rect()
        GOrect.midtop = (400, 50)
        screen.blit(GOsurf, GOrect)
        pygame.display.flip()
        time.sleep(1)


def start():
    blue = (0,0,255)
    pygame.image.load('car game/logo.jpg')
    screen.blit(logo,(200, 80))
    gFont = pygame.font.SysFont('Arial Black', 100)
    GOsurf = gFont.render('START', True, blue)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (400, 50)
    screen.blit(GOsurf, GOrect)
    pygame.display.flip()
    mc = pygame.mouse.get_pressed()
    if mc == True:
        print("Jeyaram")
    count()


# defining our gameloop function
def gameloop():
    # Music
    pygame.mixer.music.load('car game/Tokyo.mp3')
    pygame.mixer.music.play()

    # setting background image
    bg = pygame.image.load('car game/bg.jpeg')
    bgY = 100

    # setting our player
    maincar = pygame.image.load('car game\car.png')
    maincarX = 335
    maincarY = 500
    maincarX_change = 0
    maincarY_change = 0

    # other cars
    car1 = pygame.image.load('car game\car1.png')
    car1X = random.randint(178, 490)
    car1Y = 100
    car1Ychange = 0.5

    car2 = pygame.image.load('car game\car2.png')
    car2X = random.randint(178, 490)
    car2Y = 100
    car2Ychange = 0.5

    car3 = pygame.image.load('car game\car3.png')
    car3X = random.randint(178, 490)
    car3Y = 100
    car3Ychange = 0.5

    lorry = pygame.image.load('car game\lorry.png')
    lorryX = random.randint(178, 490)
    lorryY = 100
    lorryYchange = 0.5


        #Loop Program

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                # checking if any key has been pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    maincarX_change += 1

                if event.key == pygame.K_LEFT:
                    maincarX_change -= 1

                if event.key == pygame.K_UP:
                    maincarY_change -= 2

                if event.key == pygame.K_DOWN:
                    maincarY_change += 2

                # checking if key has been lifted up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0

                if event.key == pygame.K_LEFT:
                    maincarX_change = 0

                if event.key == pygame.K_UP:
                    maincarY_change = 0

                if event.key == pygame.K_DOWN:
                    maincarY_change = 0

        # setting boundary for our main car
        if maincarX < 190:
            maincarX = 190
        if maincarX > 480:
            maincarX = 480

        if maincarY < 0:
            maincarY = 0
        if maincarY > 480:
            maincarY = 480

        # CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE
        screen.fill((0, 0, 0))

        # displaying the background image

        screen.blit(bg, (0, bgY))

        # displaying our main car
        screen.blit(maincar, (maincarX, maincarY))

        # displaing other cars

        screen.blit(car1, (car1X, car1Y))
        screen.blit(car2, (car2X, car2Y))
        screen.blit(car3, (car3X, car3Y))
        screen.blit(lorry, (lorryX, lorryY))

        # updating the values
        maincarX += maincarX_change
        maincarY += maincarY_change

        # movement of the enemies
        bgY += 1
        car1Y += 1
        car2Y += 1
        car3Y += 1
        lorryY += 1

        # moving enemies infinitely

        if car1Y > 670:
            car1Y = -100
            car1X = random.randint(178, 490)
        if car2Y > 670:
            car2Y = -150
            car2X = random.randint(178, 490)
        if car3Y > 670:
            car3Y = -200
            car3X = random.randint(178, 490)
        if lorryY > 670:
            lorryY = -100
            lorryX = random.randint(178, 490)

        # moving background infinitely

        if bgY > 1:
            bgY = - 50
            

        #Collision for car1

        def isCollision(car1X, car1Y, maincarX, maincarY):
            distance = math.sqrt(math.pow(car1X - maincarX, 2) + math.pow(car1Y - maincarY, 2))

            if distance < 50:
                return True
            else:
                return False

            # Collision for car2

        def isCollision(car2X, car2Y, maincarX, maincarY):
            distance = math.sqrt(math.pow(car2X - maincarX, 2) + math.pow(car2Y - maincarY, 2))

            if distance < 50:
                return True
            else:
                return False

            # Collision for car3

        def isCollision(car3X, car3Y, maincarX, maincarY):
            distance = math.sqrt(math.pow(car3X - maincarX, 2) + math.pow(car3Y - maincarY, 2))

            if distance < 50:
                return True
            else:
                return False

            # Collision for lorry

        def isCollision(lorryX, lorryY, maincarX, maincarY):
            distance = math.sqrt(math.pow(lorryX - maincarX, 2) + math.pow(lorryY - maincarY, 2))

            if distance < 50:
                return True
            else:
                return False

            #Asign Value for Collision

        coll1 = isCollision(car1X, car1Y, maincarX, maincarY)
        coll2 = isCollision(car2X, car2Y, maincarX, maincarY)
        coll3 = isCollision(car3X, car3Y, maincarX, maincarY)
        collLorry = isCollision(lorryX, lorryY, maincarX, maincarY)

        #Collision call for car 1

        if coll1:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            lorryYchange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            ###### calling our game over function #######
            time.sleep(1)
            gameOver()

            # Collision call for car 2

        if coll2:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            ###### calling our game over function #######
            time.sleep(1)
            gameOver()

            # Collision call for car3

        if coll3:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            ###### calling our game over function #######
            time.sleep(1)
            gameOver()

            # Collision call for lorry

        if collLorry:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            ###### calling our game over function #######
            time.sleep(1)
            gameOver()

        pygame.display.update()

start()
gameloop()