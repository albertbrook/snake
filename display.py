import random
import pygame


class Display(object):
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.data = None

    def reset(self):
        self.data = [[tuple()] * self.settings.board_size[0] for _ in range(self.settings.board_size[1])]

    def draw(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j]:
                    pygame.draw.rect(self.screen, self.data[i][j],
                                     (j * self.settings.block_size + (j + 1) * self.settings.block_space,
                                      i * self.settings.block_size + (i + 1) * self.settings.block_space,
                                      self.settings.block_size, self.settings.block_size))

    def random_food(self):
        i = random.randint(0, self.settings.board_size[1] - 1)
        j = random.randint(0, self.settings.board_size[0] - 1)
        while self.data[i][j]:
            i = random.randint(0, self.settings.board_size[1] - 1)
            j = random.randint(0, self.settings.board_size[0] - 1)
        self.data[i][j] = self.settings.food_color
