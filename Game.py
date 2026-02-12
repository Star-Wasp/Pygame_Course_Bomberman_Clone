import pygame
import GameSettings as gs


class Game:
    def __init__(self, main, assets):
        # Link with main class and assets
        self.MAIN = main
        self.ASSETS = assets

    def input(self):
        for event in pygame.event.get():
            # Check if red 'x' clicked
            if event.type == pygame.QUIT:
                self.MAIN.run = False
            # Check if escape clicked
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.MAIN.run = False

    def update(self):
        pass

    def draw(self, window):
        pass