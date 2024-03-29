import pygame, sys, math, random, time
from pygame.locals import *
from Player import Player
from Shot import Shot
from Score import Score
from Alien import Alien
from Background import Background
if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

width = 900
height = 480
size = width, height

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0
bgImage = pygame.image.load("Resources/Start_Screen/StartScreen.png")
bgRect = bgImage.get_rect()

aliens = []
shots = []
player = Player(["Resources/Player/Player.png",
                "Resources/Player/Player2.png",
                "Resources/Player/Player3.png"],(5,5), (100,40),(100, height/2))

score = Score()
start = False
while True:
    bgImage = pygame.image.load("Resources/Start_Screen/StartScreen.png")
    
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    start = True
                    

        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)

    st = time.time()
    bg = Background()
    score = Score(0,(12.5,12.5))
    #Start the Game
    while start and player.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #Controls for player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("up")
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("down")
            
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("right")
                    
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("left")
                if event.key == pygame.K_SPACE:
                    if len(shots) < 2:
                        shots += [Shot(player.rect.center)]
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.direction("stop up")
                    
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.direction("stop down")
                    
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.direction("stop right")
                    
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.direction("stop left")             
                    
        #Amount of aliens allowed on screen
        if len(aliens) < 24 :
            if random.randint(0, 10) == 0:
                aliens += [Alien((-5, 0), (width, random.randint(20, height-20)))]
        
        player.update()
        player.collideWall(width, height)
        
        for alien in aliens:
            alien.update()
        for shot in shots:
            shot.update()
            shot.collideWall(width, height)
        
        #Call alien collide
        for alien in aliens:
            alien.collideWall(width, height)
            alien.collideAlien(player)
            for shot in shots:
                if shot.collide(alien):
                    score.decrease(50)
        
        score.increase(1)
        score.update()
        
        for alien in aliens:
            if not alien.living:
                aliens.remove(alien)
                
        for shot in shots:
            if not shot.living:
                shots.remove(shot)
        
        bg.update()
        
        #Blitting each image 
        screen.fill(bgColor)
        screen.blit(bg.image, bg.rect)
        for shot in shots:
            screen.blit(shot.image, shot.rect)
        for alien in aliens:
            screen.blit(alien.image, alien.rect)
        screen.blit(player.image, player.rect)
        screen.blit(score.image, score.rect)
        pygame.display.flip()
        clock.tick(60)
        
    #Loading endscreen
    bgImage = pygame.image.load("Resources/End_Screen/EndScreen.png")    
    while start and not player.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    start = False
                    aliens = []
                    shots = []
                    score = Score()
                    player = player = Player(["Resources/Player/Player.png",
                                              "Resources/Player/Player2.png",
                                              "Resources/Player/Player3.png"], (5,5), (100,40),(100, height/2))       
                    
        score.place((width/2-30, height/3))
        screen.blit(bgImage, bgRect)
        screen.blit(score.image, score.rect)
        pygame.display.flip()
        clock.tick(60)
