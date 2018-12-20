import random, os.path
import pygame

pygame.init()


size = (900, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Smash')

WHITE = (255, 255, 255)

screen.fill(WHITE)
pygame.display.flip()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False


pygame.quit()


