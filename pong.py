import pygame
from random import *

pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Pong Manu")

ball = pygame.image.load("Resources\\basket.png")
ball = pygame.transform.scale(ball,(50,50))
ballrect= ball.get_rect()
speed = [2,2]
ballrect.move_ip(0,0)

bateAbajo = pygame.image.load("Resources\\bate.png")
bateAbajo = pygame.transform.scale(bateAbajo,(170,25))
baterectAbajo = bateAbajo.get_rect()
baterectAbajo.move_ip(250,450)

bateArriba = pygame.image.load("Resources\\bate.png")
bateArriba = pygame.transform.scale(bateArriba,(170,25))
baterectArriba = bateArriba.get_rect()
baterectArriba.move_ip(250,3)

ladrillo1 = pygame.image.load("Resources\\ladrillo.png")
ladrillo1 = pygame.transform.scale(ladrillo1,(100,50))
ladrillorect1 = ladrillo1.get_rect()
ladrillorect1.move_ip(150,220)

ladrillo2 = pygame.image.load("Resources\\ladrillo.png")
ladrillo2 = pygame.transform.scale(ladrillo2,(100,50))
ladrillorect2 = ladrillo2.get_rect()
ladrillorect2.move_ip(400,220)

jugando = True

while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        baterectArriba = baterectArriba.move(-3, 0)

    if keys[pygame.K_d]:
        baterectArriba = baterectArriba.move(3, 0)

    if keys[pygame.K_LEFT]:
        baterectAbajo = baterectAbajo.move(-3,0)

    if keys[pygame.K_RIGHT]:
        baterectAbajo = baterectAbajo.move(3,0)

    if baterectAbajo.colliderect(ballrect):
        speed[1] = -speed[1]
        
    if baterectArriba.colliderect(ballrect):
        speed[1] = -speed[1]
    
    if ladrillorect1.colliderect(ballrect):
        speed[1] = -speed[1]

    if ladrillorect2.colliderect(ballrect):
        speed[1] = -speed[1]
        
    ballrect = ballrect.move(speed)
    
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
        
    ventana.fill((252,243,207))

    ventana.blit(ball,ballrect)
    ventana.blit(bateAbajo,baterectAbajo)
    ventana.blit(bateArriba, baterectArriba)
    ventana.blit(ladrillo1, ladrillorect1)
    ventana.blit(ladrillo2, ladrillorect2)

    pygame.time.Clock().tick(120)
    pygame.display.flip()

pygame.quit()

