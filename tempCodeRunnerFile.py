import pygame
import random
pygame.init()

win_width  = 1600
win_height = 1000
screen = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

list_of_X = [2,100,200,300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300,1400,1500,1558]
player = pygame.Rect((800, 900, 120, 40))
speed = 12
trail_surface = pygame.Surface((win_width, win_height), pygame.SRCALPHA)
enemy_speed_list = [10, 5, 20, 15,30,]
spawn_xs = random.sample(list_of_X, 10)
enemies = [pygame.Rect((x, 50, 40, 40)) for x in spawn_xs]

running = True
while running:
    clock.tick(60)
    trail_surface.fill((0, 0, 0, 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move_ip(-speed, 0)
    if keys[pygame.K_d]:
        player.move_ip(speed, 0)

    for enemy in enemies:
        enemy.move_ip(0, random.choice(enemy_speed_list))

        if enemy.bottom >= win_height:
            used_positions = [e.x for e in enemies if e is not enemy]
            available_xs = [x for x in list_of_X if x not in used_positions]

            if available_xs:
                enemy.x = random.choice(available_xs)
            else:
                enemy.x = random.choice(list_of_X)
            enemy.y = 50

        if player.colliderect(enemy):
            print("Game Over")
            running = False

    pygame.draw.rect(trail_surface, (100, 200, 150), player)
    for enemy in enemies:
        pygame.draw.rect(trail_surface, (200, 40, 20), enemy)

    screen.blit(trail_surface, (0, 0))
    pygame.display.update()

pygame.quit()
