import pygame.sprite

import core
from math import *
from pygame.math import *
from random import *
from pygame.time import *
from projectile import Projectile

class Player:
    def __init__(self):
        self.position = Vector3(360, 360, 0)
        self.accel = Vector2(0, 0)
        self.vitesse = Vector2(0, 0)


    def up(self):
        self.accel.xy = (int(100 * cos(radians(self.position.z))))/80, (-int(100 * sin(radians(self.position.z))))/80

    def down(self):
        self.accel.xy = (-int(100 * cos(radians(self.position.z))))/80, (int(100 * sin(radians(self.position.z))))/80

    def left(self):
        self.position.z = self.position.z - 10

    def right(self):
        self.position.z = self.position.z + 10



