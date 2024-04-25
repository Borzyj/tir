import pygame
import random

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/1.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/2.png")
target_width = 100
target_height = 100

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

font = pygame.font.Font(None, 35)

text_x = 10
text_y = 10

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
score = 0

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (target_x < mouse_x < target_x + target_width) and (target_y < mouse_y < target_y + target_height):
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1

    screen.blit(target_image, (target_x, target_y))
    text_surf = font.render(str(score), True, (255, 255, 255))
    screen.blit(text_surf, (text_x, text_y))
    pygame.display.update()

pygame.quit()