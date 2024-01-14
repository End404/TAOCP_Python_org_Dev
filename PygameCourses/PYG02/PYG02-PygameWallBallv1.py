import pygame, sys

pygame.init()
size = width, height = 600, 400
speed = [1,1]
BALCK = 0,0,0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python壁球")
ball = pygame.image.load("PYG02-ball.jpg")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]
    pygame.display.update()
    