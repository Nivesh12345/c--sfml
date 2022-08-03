
import pygame
from math import *
pygame.init()
width,height = 800,800
screen = pygame.display.set_mode((width,height),pygame.RESIZABLE)
run = True
rad= (pi/180)
angle1 = rad*0
angle2 = rad*90
angle3 = rad*180
angle4 = rad*270
xpos,ypos = width/2,height/2
clock = pygame.time.Clock()
qw = 400
dis = 200
di = 0
ds= sqrt(2)*qw
speed = rad
sx = 2
widline = 5
color = "black"
while run:
    screen.fill("white")
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            event.pos
    # ---------------------firstpoint------------------       
    ex1 = (cos(angle1)*dis)+ 300
    ey1 = (sin(angle1)*dis)+ 300
    angle1 -=speed
    # ---------------------secondpoint------------------       
    ex2 = (cos(angle2)*dis)+ 300 
    ey2 = (sin(angle2)*dis)+ 300
    angle2 -=speed
    # ---------------------thirdpoint------------------       
    ex3 = (cos(angle3)*dis)+ 300 
    ey3 = (sin(angle3)*dis)+ 300
    angle3 -=speed
    # ---------------------fouthpoint------------------       
    ex4 = (cos(angle4)*dis)+ 300
    ey4 = (sin(angle4)*dis)+ 300
    angle4 -=speed

    # ---------------------firstpoint------------------       
    zex1 = (cos(angle1)*(dis-di))+ qw
    zey1 = (sin(angle1)*(dis-di))+ qw
    angle1 -=speed
    # ---------------------secondpoint------------------       
    zex2 = (cos(angle2)*(dis-di))+ qw 
    zey2 = (sin(angle2)*(dis-di))+ qw
    angle2 -=speed
    # ---------------------thirdpoint------------------       
    zex3 = (cos(angle3)*(dis-di))+ qw 
    zey3 = (sin(angle3)*(dis-di))+ qw
    angle3 -=speed
    # ---------------------fouthpoint------------------       
    zex4 = (cos(angle4)*(dis-di))+ qw
    zey4 = (sin(angle4)*(dis-di))+ qw
    angle4 -=speed

    # dis-=sx
    # if dis <-250:
    #     sx = -sx
    # if dis>250:
    #     sx = -sx
    # ---------------------------------endofpoints--------------------
    # p1 =                #(300,400)                           #(ex1,ey1)
    # p2 =                #(400,300)                            #(ex2,ey2)
    # p3 =                #(300,200)                            #(ex3,ey3)
    # p4 =                #(200,300)                            #(ex4,ey4)
    p1 =  (ex1,ey1)
    p2 = (ex2,ey2)
    p3 =(ex3,ey3)
    p4 =  (ex4,ey4)     
    zp1 =  (zex1,zey1)
    zp2 = (zex2,zey2)
    zp3 =(zex3,zey3)
    zp4 =  (zex4,zey4)              

    # pygame.draw.circle(screen,"white",(xpos,ypos),30)
    pygame.draw.circle(screen,"red",p1,10)
    pygame.draw.circle(screen,"red",p2,10)
    pygame.draw.circle(screen,"red",p3,10)
    pygame.draw.circle(screen,"red",p4,10)
    pygame.draw.circle(screen,"red",zp1,10)
    pygame.draw.circle(screen,"red",zp2,10)
    pygame.draw.circle(screen,"red",zp3,10)
    pygame.draw.circle(screen,"red",zp4,10)
    # rectangle =pygame.draw.rect(screen,"white",(ex,ey,60,60))
    pygame.draw.line(screen,color,p1,p2,widline)
    pygame.draw.line(screen,color,p2,p3,widline)
    pygame.draw.line(screen,color,p3,p4,widline)
    pygame.draw.line(screen,color,p4,p1,widline)
    pygame.draw.line(screen,color,zp1,zp2,widline)
    pygame.draw.line(screen,color,zp2,zp3,widline)
    pygame.draw.line(screen,color,zp3,zp4,widline)
    pygame.draw.line(screen,color,zp4,zp1,widline)

    pygame.draw.line(screen,color,p1,zp1,widline)
    pygame.draw.line(screen,color,p2,zp2,widline)
    pygame.draw.line(screen,color,p3,zp3,widline)
    pygame.draw.line(screen,color,p4,zp4,widline)
    # pygame.draw.line(screen,"white",p3,p1)
    # pygame.draw.line(screen,"white",p2,p4)
    
    pygame.display.update()
pygame.quit()
