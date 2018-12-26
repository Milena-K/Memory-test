import pygame

class Box:

    def __init__(self, surface, color, rect, value):
        self.surface = surface
        self.color = color
        self.rect = rect
        self.value = value
        self.font_size = int(self.rect[2])
        self.font = pygame.font.SysFont("Times New Roman", self.font_size)
        pygame.draw.rect(self.surface, self.color, self.rect, 1)
        label = self.font.render(str(self.value), 1, self.color)
        if not self.value == 0:
            self.surface.blit(label, (self.rect[0] + (self.rect[2]/2) - (self.font_size/4), self.rect[1]))

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos[0] > self.rect[0] and mouse_pos[0] < self.rect[0] + self.rect[2] and mouse_pos[1] > self.rect[1] and mouse_pos[1] < self.rect[1] + self.rect[3]
