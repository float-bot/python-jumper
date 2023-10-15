import pygame
from pygame.locals import *
from pygame.sprite import _Group

pygame.init()

vec=pygame.math.Vector2

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRICTION = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")