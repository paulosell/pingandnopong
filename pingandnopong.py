import pygame
import random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(10,10)
    return (x//10*10, y//10 * 10)

def restart():
    ball_pos = on_grid_random()
    score = 0

def collide(surface,ball):
    flag = False
    for i in range(len(surface)):
        if surface[i][0] == ball[0] and surface[i][1] == ball[1]:
            flag = True 
    return flag

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
WHITE = (255,255,255)


score = 0
pygame.init()
myfont = pygame.font.SysFont("monospace", 16)
WHITE = (255,255,255)

score = 0
max_score = score


screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

surface = [(280,590),(290,590),(300,590),(310,590),(320,590)]
surface_skin = pygame.Surface((10,10))
surface_skin.fill((255,255,255))

ball = pygame.Surface((10,10))
ball.fill((255,0,0))
ball_pos = on_grid_random()
my_direction = -1
clock = pygame.time.Clock()
speed = 20
while True:
    clock.tick(speed)
    has_event = False
    for event in pygame.event.get():
        if event.type == QUIT:
            
            pygame.quit()
        
        if event.type == KEYDOWN:
            
            if event.key == K_RIGHT:
                my_direction = RIGHT
            if event.key == K_LEFT:
                my_direction = LEFT
        if event.type == KEYUP:
            my_direction = -1
            
    
    
    if my_direction == LEFT:        
        if surface[0][0] != 0:
            for i in range(len(surface)):
                surface[i] = (surface[i][0] - 10, surface[i][1])

    if my_direction == RIGHT:        
        if surface[4][0] != 590:
            for i in range(len(surface)):
                surface[i] = (surface[i][0] + 10, surface[i][1])
    
    
    screen.fill((0,0,0))
    
    if collide(surface, ball_pos):
        ball_pos = on_grid_random()
        score += 1
        speed+=5
    else:
        ball_pos = (ball_pos[0], ball_pos[1]+10)
    
    if ball_pos[1] >= 600:
        if score > max_score:
            max_score = score
        ball_pos = on_grid_random()
        score = 0
        speed = 20


    screen.blit(ball, ball_pos)
    
    for pos in surface:
        screen.blit(surface_skin,pos)  
   

    scoretext = myfont.render("score", 1, (255,255,255))
    maxscoretext = myfont.render("max" , 1, (255,255,255))

    scorevalue = myfont.render(str(score),1,(255,255,255))
    maxscorevalue = myfont.render(str(max_score),1,(255,255,255))

    screen.blit(scoretext, (500, 10))
    screen.blit(maxscoretext, (500, 20))

    screen.blit(scorevalue,(560,10))
    screen.blit(maxscorevalue,(560,20))
   
    pygame.display.update()
