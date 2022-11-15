import core
from math import *
from pygame.math import *
from random import *
from pygame.time import *


class Player:
    def __init__(self, j="J0", x=0, y=0, z=0, ax=0, ay=0, vx=0, vy=0):
        self.position = Vector3(x, y, z)
        self.name = j
        self.accel = Vector2(ax, ay)
        self.vitesse = Vector2(vx, vy)

    def up(self):
        self.accel.xy = (int(100 * cos(radians(self.position.z))))/80, (-int(100 * sin(radians(self.position.z))))/80

    def down(self):
        self.accel.xy = (-int(100 * cos(radians(self.position.z))))/80, (int(100 * sin(radians(self.position.z))))/80

    def left(self):
        self.position.z = self.position.z - 10

    def right(self):
        self.position.z = self.position.z + 10

class Projectile:
    def __init__(self,k="K0", px=0, py=0, pz=0, avx=0, avy=0):
        self.name = k
        self.pos = Vector3(px, py, pz)
        self.vit = Vector2(avx, avy)

    def shoot(self):
        self.vit.xy = (int(100 * cos(radians(self.pos.z))))/80, (-int(100 * sin(radians(self.pos.z))))/80