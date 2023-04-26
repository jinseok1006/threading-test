import pygame
from src.constant import SCREEN_WIDTH, SCREEN_HEIGHT


class Character:
    # static member
    speed = 0.1

    def __init__(self):
        self.img = pygame.image.load("./assets/character.png")
        self.size = self.img.get_rect().size
        self.posX = (SCREEN_WIDTH / 2) - (self.size[0] / 2)
        self.posY = SCREEN_HEIGHT - self.size[1]

        self.toRight = 0
        self.toLeft = 0
        self.toUp = 0
        self.toDown = 0

    def move(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            print("keydown")
            if event.key == pygame.K_LEFT:
                self.toLeft = -Character.speed
            elif event.key == pygame.K_RIGHT:
                self.toRight = Character.speed
            elif event.key == pygame.K_DOWN:
                self.toDown = Character.speed
            elif event.key == pygame.K_UP:
                self.toUp = -Character.speed

        if event.type == pygame.KEYUP:
            print("keyup")
            if event.key == pygame.K_LEFT:
                self.toLeft = 0
            if event.key == pygame.K_RIGHT:
                self.toRight = 0
            if event.key == pygame.K_UP:
                self.toUp = 0
            if event.key == pygame.K_DOWN:
                self.toDown = 0

    def update(self, dt: int):
        # 둘이 변화량이 같으면 계산하지마라
        if self.toRight != self.toLeft:
            self.posX += self.toLeft * dt + self.toRight * dt
        if self.toUp != self.toDown:
            self.posY += self.toUp * dt + self.toDown * dt

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.img, (self.posX, self.posY))


class Dummy:
    pass
