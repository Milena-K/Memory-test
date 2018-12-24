import pygame

pygame.init()

size = (1000, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Instant memory test")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(WHITE)


# rect(Surface, color, Rect, width=0)
def draw_matrix(Surface, color, Rect):
    pygame.draw.rect(screen, BLACK, Rect, 1)
    





is_running = True
while is_running:
    Rect = (50, 50, 500, 500)
    draw_matrix(screen, BLACK, Rect)
    pygame.display.flip()

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             is_running = False


pygame.quit()

