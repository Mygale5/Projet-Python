import pygame
from pygame.math import *
from math import *
import core
from core import Texture

class Projectile(pygame.sprite.Sprite):
    def __init__(self, core):
        super().__init__()
        self.velocity = 5
        self.image = core.Texture.load('https://imgur.com/a/IDlv8MV')
        self.rect = self.image.get_rect()


'''
    def shoot(self):
        self.vit.xy = (3*int(100 * cos(radians(self.pos.z))))/80, (3*-int(100 * sin(radians(self.pos.z))))/80
'''
