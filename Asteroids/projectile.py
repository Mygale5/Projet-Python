import pygame
from pygame.math import *
from math import *
import core

'Assets/projectile.png'

'''class Projectile():

    def __init__(self):
        self.pos = Vector3(0, 0, 0)
        self.velocity = Vector2(0, 0)
        self.url = 'Assets/projectile.png'
        self.temps = [0]
        self.aff = None
        self.display = True

    def affichage(self):
        self.aff = core.Texture.show()

    def apllyvit(self):
        self.velocity = (3*int(100 * cos(radians(self.pos.z))))/80, (3*-int(100 * sin(radians(self.pos.z))))/80
'''
'''
    def shoot(self):
        self.vit.xy = (3*int(100 * cos(radians(self.pos.z))))/80, (3*-int(100 * sin(radians(self.pos.z))))/80
'''
class Projectile():
    def __init__(self, offset=0, scaleSize=(100, 100), display=True, alpha=255):
        self.ready = False
        self.sprit = None
        self.url = 'Assets/projectile.png'
        self.w = None
        self.h = None
        self.pos = Vector3(0, 0, 0)
        self.velocity = Vector2(0, 0)
        self.scaleSize = scaleSize
        self.offset = offset
        self.display = display
        self.alpha = alpha
        self.box=False

    def load(self):

        self.sprit = pygame.image.load(self.url).convert_alpha()
        self.sprit = pygame.transform.scale(self.sprit, self.scaleSize)
        self.w = self.sprit.get_width()
        self.h = self.sprit.get_height()
        self.ready = True

    def show(self):
        if self.display:
            if self.box:
                core.Draw.rect((0,255,0),(self.pos.x,self.pos.y,self.w,self.h),1)
            if self.ready:
                #self.sprit.set_alpha(self.alpha)
                #core.screen.blit(self.sprit, self.pos)
                core.screen.blit(self.sprit, self.pos.xy)

    def apllyvit(self):
        self.velocity = (3*int(100 * cos(radians(self.pos.z))))/80, (3*-int(100 * sin(radians(self.pos.z))))/80
        self.pos.xy += self.velocity


