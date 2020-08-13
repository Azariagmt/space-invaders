import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1080,650))

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

player_image = pygame.image.load('space-invaders.png')
player_position_X = 510
player_position_Y = 530
player_position_change = 0

enemy_image = pygame.image.load('bad-guys.png')
enemy_position_X = random.randint(0,800)
enemy_position_Y = random.randint(50,150)
enemy_position_X_change = 4
enemy_position_Y_change = 40

background_image = pygame.image.load('2663927.jpg')

def player(x, y):
    screen.blit(player_image,(x,y))

def enemy(x, y):
    screen.blit(enemy_image, (x,y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_position_change = - 5
            if event.key == pygame.K_RIGHT:
                player_position_change = + 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('key release')

    player_position_X += player_position_change
    enemy_position_X += enemy_position_X_change

    if enemy_position_X <= 0:
        enemy_position_X_change = 5
        enemy_position_Y += enemy_position_Y_change
    elif enemy_position_X >=1016:
        enemy_position_X_change = -5
        enemy_position_Y += enemy_position_Y_change

    if player_position_X <= 0:
        player_position_X = 0
    elif player_position_X >=1016:
        player_position_X =1016

    screen.fill((254, 156, 99))
    screen.blit(background_image, (0,0))
    player(player_position_X,player_position_Y)
    enemy(enemy_position_X, enemy_position_Y)
    pygame.display.update()


