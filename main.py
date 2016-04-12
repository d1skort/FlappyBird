import sys
import random
import pygame
from pygame.locals import *


class FlappyBird(object):
    def __init__(self):
        pygame.font.init()
        self.screen = pygame.display.set_mode((400, 708))
        self.background = pygame.image.load("assets/background.png").convert_alpha()
        self.wall_up = pygame.image.load("assets/bottom.png").convert_alpha()
        self.wall_down = pygame.image.load("assets/top.png").convert_alpha()
        self.bird = pygame.Rect(65, 50, 50, 50)
        self.bird_sprites = [
            pygame.image.load("assets/0.png").convert_alpha(),
            pygame.image.load("assets/1.png").convert_alpha(),
            pygame.image.load("assets/dead.png").convert_alpha()
        ]
        self.bird_y = 50
        self.dead = False
        self.sprite = 0
        self.gravity = 5
        self.jump_speed = 10
        self.jump = 0
        self.wallx = 400
        self.gap = 125
        self.offset = random.randrange(-110, 111)
        self.counter = 0

    def update_walls(self):
        self.wallx -= 3
        if self.wallx < -99:
            self.wallx = 400
            self.offset = random.randrange(-110, 111)
            self.counter += 1

    def update_bird(self):
        if self.jump:
            self.jump_speed -= 1
            self.bird[1] -= self.jump_speed
            self.jump -= 1
        else:
            self.bird[1] += self.gravity
            self.gravity += 0.2

        up_rect = pygame.Rect(
            self.wallx,
            360 + self.gap + self.offset + 10,
            self.wall_up.get_width() - 10,
            self.wall_up.get_height()
        )

        down_rect = pygame.Rect(
            self.wallx,
            0 - self.gap + self.offset - 10,
            self.wall_down.get_width() - 10,
            self.wall_down.get_height(),
        )

        if up_rect.colliderect(self.bird):
            self.dead = True
        if down_rect.colliderect(self.bird):
            self.dead = True

        if not 0 < self.bird[1] < 720:
            self.wallx = 400
            self.dead = False
            self.offset = random.randrange(-110, 111)
            self.gravity = 5
            self.jump_speed = 10
            self.bird[1] = 50
            self.counter = 0

    def run(self):
        clock = pygame.time.Clock()
        #font = pygame.font.SysFont("Arial", 50)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit()
                if event.type == KEYDOWN and not self.dead:
                    self.jump = 17
                    self.gravity = 5
                    self.jump_speed = 10

            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wall_down, (self.wallx, 0 - self.gap + self.offset))
            self.screen.blit(self.wall_up, (self.wallx, 360 + self.gap + self.offset))
         #   self.screen.blit(font.render(str(self.counter), -1, (255, 255, 255)), (190, 50))
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1
            self.screen.blit(self.bird_sprites[self.sprite], (50, self.bird[1]))
            if not self.dead:
                self.sprite = 0
            self.update_walls()
            self.update_bird()
            pygame.display.update()


if __name__ == '__main__':
    FlappyBird().run()
