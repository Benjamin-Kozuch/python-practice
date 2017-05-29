#With inspiration from http://www.nerdparadise.com/programming/pygame/part1

import pygame
pygame.init()

#Makes a black screen pop-up
screen = pygame.display.set_mode((600, 400))  # w,h

#Need this to change the F/S frames per second later.
clock = pygame.time.Clock()

#Ball
x_ball = 570
y_ball = 30
ball_x_direction = -1 # (1) = right and (-1) = left
ball_y_direction = 1
ball_speed = 5

#Paddle
x_paddle = 30
y_paddle = 30


done = False
while not done:
    for event in pygame.event.get():
   
        if event.type == pygame.QUIT:
            done = True

    
    if pygame.key.get_pressed()[pygame.K_UP]: y_paddle -= 3
    if pygame.key.get_pressed()[pygame.K_DOWN]: y_paddle += 3
    
    x_ball += ball_speed*ball_x_direction
    y_ball += ball_speed*ball_y_direction
   




    screen.fill((255, 255, 255)) #without this the moving around square would leave a trailing tail.
    #if is_blue: color = (0, 128, 255)
    #else: color = (255, 100, 0)
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x_ball, y_ball, 10, 10))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x_paddle, y_paddle, 10, 60))
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(560, 0, 10, 400)) #right side


    pygame.display.flip()
    clock.tick(120)



