import pygame
from pygame.math import *
from math import *
import core
from core import Texture

core.memory("url", Texture('S3\Asteroids\Assets\projectile.png'))

class Projectile():
    def __init__(self):
        self.pos = Vector3(0, 0, 0)
        self.velocity = Vector2(0, 0)
        self.deftext = core.Texture.load(core.memory("url"))
        self.temps = [0]


    def affichage(self):
        self.affichage = core.Texture.show(core.memory("url"))

    def apllyvit(self):
        self.velocity = (3*int(100 * cos(radians(self.pos.z))))/80, (3*-int(100 * sin(radians(self.pos.z))))/80

'''
    def shoot(self):
        self.vit.xy = (3*int(100 * cos(radians(self.pos.z))))/80, (3*-int(100 * sin(radians(self.pos.z))))/80
'''
