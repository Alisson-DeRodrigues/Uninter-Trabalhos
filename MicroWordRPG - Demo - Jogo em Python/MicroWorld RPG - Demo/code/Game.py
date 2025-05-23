import pygame, sys
from code.Const import *
from code.Level import Level

class Game:
    def __init__(self):

        # window setup
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('MicroWorld: RPG - Demo')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.window.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
