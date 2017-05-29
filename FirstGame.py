import pygame
pygame.init()

#Makes a black screen pop-up
screen = pygame.display.set_mode((1000, 300))  # w,h

done = False
is_blue = True



while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.QUIT:
            done = True

    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    pygame.display.flip()


