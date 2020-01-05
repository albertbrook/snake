import pygame


class Functions(object):
    def __init__(self, settings, screen, display, snake):
        self.settings = settings
        self.screen = screen
        self.display = display
        self.snake = snake

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    self.snake.horizontal = -1
                    self.snake.vertical = 0
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    self.snake.horizontal = 1
                    self.snake.vertical = 0
                elif event.key in [pygame.K_w, pygame.K_UP]:
                    self.snake.horizontal = 0
                    self.snake.vertical = -1
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.snake.horizontal = 0
                    self.snake.vertical = 1
            elif event.type == pygame.USEREVENT:
                self.snake.move()

    def draw_screen(self):
        self.screen.fill(self.settings.background)
        self.display.draw()
        pygame.display.flip()
