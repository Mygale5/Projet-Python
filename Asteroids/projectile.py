import pygame
from pygame.math import *
from math import *
import core

class Projectile():
    def __init__(self, player):
        super().__init__()
        self.pos = Vector3(0, 0, 0)
        self.test = 0
        self.vit = Vector2(0, 0)


    def shoot(self):
        self.vit.xy = (3*int(100 * cos(radians(self.pos.z))))/80, (3*-int(100 * sin(radians(self.pos.z))))/80

    def proj1(self):
        core.Draw.circle([0, 255, 0], (self.pos.x, self.pos.y), 2.5)

    def proj2(self):
        core.Draw.circle([0, 0, 255], (self.pos.x, self.pos.y), 2.5)

    def proj3(self):
        core.Draw.circle([0, 255, 255], (self.pos.x, self.pos.y), 2.5)

    def proj4(self):
        core.Draw.circle([100, 255, 0], (self.pos.x, self.pos.y), 2.5)

    def proj5(self):
        core.Draw.circle([255, 255, 0], (self.pos.x, self.pos.y), 2.5)
