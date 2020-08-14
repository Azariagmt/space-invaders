import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((1080, 650))

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

mixer.music.load('sounds/meow.wav')
mixer.music.play(-1)

# player
player_image = pygame.image.load('space-invaders.png')
player_position_X = 510
player_position_Y = 530
player_position_change = 0

# score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_X = 10
text_Y = 10


def show_score(x, y):
    sc = font.render('Score : ' + str(score), True, (255, 255, 255))
    screen.blit(sc, (x, y))

# enemy
enemy_image = []
enemy_position_X = []
enemy_position_Y = []
enemy_position_X_change = []
enemy_position_Y_change = []
number_of_enemies = 6

for _ in range(number_of_enemies):
    enemy_image.append(pygame.image.load('bad-guys.png'))
    enemy_position_X.append(random.randint(0, 800))
    enemy_position_Y.append(random.randint(50, 150))
    enemy_position_X_change.append(4)
    enemy_position_Y_change.append(40)

# bullet
bullet_image = pygame.image.load('bullet.png')
bullet_position_Y = 530
bullet_position_X = 0
bullet_position_Y_change = 10
bullet_state = 'ready'

background_image = pygame.image.load('2663927.jpg')


def player(x, y):
    screen.blit(player_image, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_image[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x + 16, y + 10))


def check_collision(enemy_position_X, enemy_position_Y,
                    bullet_position_X, bullet_position_Y):
    distance = math.sqrt(
        math.pow(enemy_position_X - bullet_position_X, 2) + (math.pow(enemy_position_Y - bullet_position_Y, 2)))
    if distance < 27:
        return True


running = True
while running:

    screen.fill((254, 156, 99))
    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_position_change = - 6
            if event.key == pygame.K_RIGHT:
                player_position_change = + 6
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    mixer.Sound('sounds/bullet.wav').play()
                    bullet_position_X = player_position_X
                    fire_bullet(bullet_position_X, bullet_position_Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('key release')

    player_position_X += player_position_change

    for i in range(number_of_enemies):
        enemy_position_X[i] += enemy_position_X_change[i]
        if enemy_position_X[i] <= 0:
            enemy_position_X_change[i] = 5
            enemy_position_Y[i] += enemy_position_Y_change[i]
        elif enemy_position_X[i] >= 1016:
            enemy_position_X_change[i] = -5
            enemy_position_Y[i] += enemy_position_Y_change[i]

        if check_collision(enemy_position_X[i], enemy_position_Y[i], bullet_position_X, bullet_position_Y):
            mixer.Sound('sounds/ouch.wav').play()
            bullet_position_Y = 530
            bullet_state = 'ready'
            score += 1
            print(score)
            enemy_position_X[i] = random.randint(0, 800)
            enemy_position_Y[i] = random.randint(50, 150)

        enemy(enemy_position_X[i], enemy_position_Y[i], i)

    if player_position_X <= 0:
        player_position_X = 0
    elif player_position_X >= 1016:
        player_position_X = 1016

    # bullet persisting movement
    if bullet_state == 'fire':
        fire_bullet(bullet_position_X, bullet_position_Y)
        bullet_position_Y -= bullet_position_Y_change
        if bullet_position_Y <= 0:
            bullet_position_Y = 530
            bullet_state = 'ready'

    player(player_position_X, player_position_Y)
    show_score(text_X, text_Y)
    pygame.display.update()
