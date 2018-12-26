import random
from box import Box


class Grid:

    def __init__(self, order, surface, color, screen_size):
        self.order = order
        self.boxes = []
        self.surface = surface
        self.color = color
        self.screen_size = screen_size
        
    def draw(self):
        values = []
        for i in range(self.order**2):
            if i < 10:
                values.append(i)
            else:
                values.append(0)
                
        random.shuffle(values)
        
        
        for i in range(self.order):
            for j in range(self.order):
                self.boxes.append(Box(self.surface, self.color, (i*self.screen_size[0]/self.order, j*self.screen_size[1]/self.order, self.screen_size[0]/self.order, self.screen_size[1]/self.order), values[0]))
                values.pop(0)
                    
    def get_boxes(self):
        return self.boxes
