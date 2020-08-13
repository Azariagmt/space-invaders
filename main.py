import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

player_image = pygame.image.load('space-invaders.png')
position_X = 370
position_Y = 480

def player(x,y):
    screen.blit(player_image,(x,y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left press')
                position_X = position_X - 2
            elif event.key == pygame.K_RIGHT:
                print('right press')
                position_X = position_X + 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('key release')

    screen.fill((254, 156, 99))
    player(position_X,position_Y)
    pygame.display.update()


