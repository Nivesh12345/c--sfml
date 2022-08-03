import pygame
from math import *
pygame.init()
width,height = 800,800
screen = pygame.display.set_mode((width,height))
run = True
xpos = width/2
ypos = height/2
# angle = 0
clock = pygame.time.Clock()
class planet():
    angle = 0
    rad= (pi/180)
    def __init__(self,distance,radius,color,speed,angle) -> None:
        # self.x =x
        self.distance =distance
        # self.y = y
        self.angle = angle
        self.speed = speed
        self.radius = radius
        self.color = color
        # planet.angle = self.angle
    def move(self):
        ex =(cos(self.angle*planet.rad)*self.distance)+xpos
        ey =(sin(self.angle*planet.rad)*self.distance)+ypos
        
        self.angle+=self.speed
        pygame.draw.circle(screen,self.color,(ex,ey),self.radius)
        pygame.draw.circle(screen,self.color,(xpos,ypos),self.distance,2)
        pygame.draw.line(screen,self.color,(ex,ey),(xpos,ypos),3)
        
h= planet(200,20,"green",4,90)  
j= planet(250,20,"orange",3,180)  
k= planet(300,20,"blue",2,270)  
l= planet(350,20,"purple",1,360)  

while run:
    screen.fill("black")
    clock.tick(80)
    j.move()
    h.move()
    k.move()
    l.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    pygame.draw.circle(screen,"yellow",(xpos,ypos),30)
    # pygame.draw.line(screen,"white",(xpos+150,ypos),(xpos+100,ypos),2)
    pygame.display.update()
pygame.quit()
