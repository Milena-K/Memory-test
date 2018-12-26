import pygame
from grid import Grid

pygame.init()

screen_size = (1000, 1000)
screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Instant memory test")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(WHITE)

grid = Grid(4, screen, BLACK, screen_size)
grid.draw()
boxes = grid.get_boxes()
last_clicked = 0
playing = True

while playing:
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                if box.is_hovered():
                    if not box.value == last_clicked + 1:
                        playing = False
                    else:
                        last_clicked = box.value

        if event.type == pygame.QUIT:
            playing = False


pygame.quit()
