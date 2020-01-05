class Settings(object):
    def __init__(self):
        self.block_size = 30
        self.block_space = 0
        self.block_color = (255, 255, 255)

        self.board_size = (30, 20)

        self.screen_size = ((self.block_size + self.block_space) * self.board_size[0] + self.block_space,
                            (self.block_size + self.block_space) * self.board_size[1] + self.block_space)
        self.background = (0, 0, 0)

        self.food_color = (255, 0, 0)

        self.snake_speed = 100
