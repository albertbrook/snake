import pygame


class Snake(object):
    def __init__(self, settings, display):
        self.settings = settings
        self.display = display

        self.data = self.horizontal = self.vertical = None
        self.reset()

    def reset(self):
        self.display.reset()
        self.data = [[0, 0], [0, 1], [0, 2]]
        self.display_snake()
        self.display.random_food()
        self.horizontal = 1
        self.vertical = 0
        pygame.time.set_timer(pygame.USEREVENT, self.settings.snake_speed)

    def display_snake(self):
        for body in self.data:
            self.display.data[body[0]][body[1]] = self.settings.block_color

    def move(self):
        temp = [self.data[-1][0] + self.vertical, self.data[-1][1] + self.horizontal]
        if not (0 <= temp[1] < self.settings.board_size[0]) or not (0 <= temp[0] < self.settings.board_size[1]):
            self.reset()
            return
        for body in range(len(self.data) - 1):
            if self.data[body] == temp:
                if body == len(self.data) - 2:
                    self.horizontal = -self.horizontal
                    self.vertical = -self.vertical
                    return self.move()
                self.reset()
                return
        if self.display.data[temp[0]][temp[1]]:
            self.data.append(temp)
            self.display.random_food()
        else:
            self.display.data[self.data[0][0]][self.data[0][1]] = tuple()
            for body in range(len(self.data) - 1):
                self.data[body], self.data[body + 1] = self.data[body + 1], self.data[body]
            self.data[-1] = temp
        self.display_snake()
