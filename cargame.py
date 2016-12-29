# 1 - Import library
import pygame
import time
import random
from pygame.locals import *
 
# 2 - Initialize the game
pygame.init()
width, height = 700, 580
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
x=200
y=300
dx=0
dy=0
ph=random.randrange(1,3)*50
th=random.randrange(1,3)*50
tx=200+(120+5)*random.randrange(0,2)
px=200+(120+5)*random.randrange(2,4)
py=0
ty=0
ttime=0
ptime=0
score=0
#class truck:
    
clock=pygame.time.Clock()
screen=pygame.display.set_mode((width, height))
# pygame.display.set_caption('Game')
# 3 - Load images
road = pygame.image.load("high.jpg")
player = pygame.image.load("car.jpg")
font=pygame.font.SysFont(None,40)
sfont=pygame.font.SysFont(None,30)
# 4 - keep looping through
while 1:
    
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        print(event)
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        if event.type == KEYDOWN:
            if event.key == K_UP:
                 y=y-20
            elif event.key == K_DOWN:
                y=y+20
            elif event.key == K_LEFT:
                x=x-125
            elif event.key == K_RIGHT:
                x=x+125
        '''elif event.type == KEYUP:
            if event.key == K_UP:
                 dy=0
            elif event.key == K_DOWN:
                dy=0
            elif event.key == K_LEFT:
                dx=0
            elif event.key == K_RIGHT:
                dx=0 '''          

    py=pygame.time.get_ticks()/5   #right 
    ty=pygame.time.get_ticks()/13   #left
    x=x+dx
    y=y+dy
    # 5 - clear the screen before drawing it again
    screen.fill(white)
    # 6 - draw the screen elements
    screen.blit(road, (200,0)) 
    screen.blit(player, (x,y))
    screen.fill(black,[195,0,5,1000])
    screen.fill(black,[px,py-ptime,120,ph])
    screen.fill(black,[tx,ty-ttime,120,th])
    screen.fill(black,[700,0,5,1000])
    screentext=sfont.render("Score: "+str(score),True,green)
    screen.blit(screentext,(20,50))
    def messagetoscreen(msg,color):
          screentext=font.render(msg,True,color)
          screen.blit(screentext,[300,100])

    # 7 - update the screen
    pygame.display.update()
    clock.tick(30)
    if(ty-ttime>578):
         score=score+1
         pygame.display.update()
         ttime=ty
         tx=200+(120+5)*random.randrange(0,2)
         th=random.randrange(1,3)*50
    if(py-ptime>578):
         score=score+1
         pygame.display.update()     
         ptime=py
         px=200+(120+5)*random.randrange(2,4)
         ph=random.randrange(1,3)*50
    if x< 200 or x>605:
         messagetoscreen("You hit boundary",red)        
         pygame.display.update()
         time.sleep(1)
         pygame.quit()
         exit(0)  
    if(ty+th-ttime>y and ty-ttime<y+228 and x==tx ):
         messagetoscreen("Got hitten while ovvertaking",red)
         pygame.display.update()
         time.sleep(1)
         pygame.quit()
         exit(0)
    if(py+ph-ptime>y and py-ptime<y+228 and x==px ):
         messagetoscreen("You hit in opposite lane",red)
         pygame.display.update()
         time.sleep(1)
         pygame.quit()
         exit(0)
