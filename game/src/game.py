from typing import List
import os
import pygame

from src.constant import SCREEN_WIDTH, SCREEN_HEIGHT
from src.character import Character


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.backgroundImg = pygame.image.load("./assets/background.png")
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.myChar = Character()

    def loop(self):
        while self.running:
            self.dt = self.clock.tick(60)
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pygame.event.get():
            # 종료 이벤트
            if event.type == pygame.QUIT:
                self.running = False

            # 캐릭터 이동 이벤트
            self.myChar.move(event)

    def update(self):
        self.myChar.update(self.dt)

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.myChar.draw(self.screen)
        pygame.display.update()
