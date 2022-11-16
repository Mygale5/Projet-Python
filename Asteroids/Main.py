'''import core
from math import *
from pygame.math import *
from random import *


def setup():
    core.fps = 10
    core.WINDOW_SIZE = [500, 500]
    core.memory('astePos', Vector3(randint(100, 200), randint(100, 200), 0))
    core.memory("bobHistorique", [])
    core.memory('origine', Vector2(450, 450))
    core.memory("angletest", 0)

def run():
    show()
    move()
    core.printMemory()
    if len(core.memory("bobHistorique")) > 1:
        core.Draw.lines([255, 255, 255], False, core.memory('bobHistorique'), 3)
    if core.getKeyPressList("r"):
        core.memory("astePos", Vector3(0, 0, 0))
        core.memory("bobHistorique", [])


def show():
    core.cleanScreen()
    p1 = Vector2(core.memory("astePos").x, core.memory("astePos").y) + Vector2(-5, 0).rotate(core.memory("astePos").z)
    # p1.y = -p1.y
    # p1 = p1 + core.memory("origine")

    p2 = Vector2(core.memory("astePos").x, core.memory("astePos").y) + Vector2(0, 15).rotate(core.memory("astePos").z)
    # p2.y = -p2.y
    # p2 = p2 + core.memory("origine")

    p3 = Vector2(core.memory("astePos").x, core.memory("astePos").y) + Vector2(5, 0).rotate(core.memory("astePos").z)
    # p3.y = -p3.y
    # print(p3.y)
    # p3 = p3 + core.memory("origine")

    core.Draw.polygon([255, 0, 0], (p1, p2, p3))


def move():
    core.memory("bobHistorique").append(Vector2(core.memory("astePos").x, core.memory("astePos").y))

    vel = Vector2(0, 1)
    angle = (vel.angle_to(Vector2(0, 1)) + core.memory("astePos").z) % 360
    posx = core.memory("astePos").x + vel.x
    posy = core.memory("astePos").y + vel.y
    core.memory("astePos", Vector3(posx, posy, angle))



core.main(setup, run)


import core
from math import *
from pygame.math import *
from random import *
from player import Player

def setup():
    core.fps = 10
    core.WINDOW_SIZE = [500, 500]
    core.memory('astePos', Player("J0", 250 ,250 ,0))
    core.memory("bobHistorique", [])
    core.memory('origine', Vector2(450, 450))
    core.printMemory()

def run():
    show()
    touches()
    #move()

def show():
    core.cleanScreen()
    p1 = Vector2(core.memory("astePos").position.x, core.memory("astePos").position.y) + Vector2(-5, 0).rotate(core.memory("astePos").position.z)

    p2 = Vector2(core.memory("astePos").position.x, core.memory("astePos").position.y) + Vector2(0, 15).rotate(core.memory("astePos").position.z)

    p3 = Vector2(core.memory("astePos").position.x, core.memory("astePos").position.y) + Vector2(5, 0).rotate(core.memory("astePos").position.z)

    core.Draw.polygon([255, 0, 0], (p1, p2, p3))


def move():

    vel = Vector2(0, 1)
    angle = (vel.angle_to(Vector2(0, 1)) + core.memory("astePos").z) % 360
    core.memory("astePos").x += vel.x
    core.memory("astePos").y += vel.y



def touches():
    if core.getKeyPressList("z"):
        core.memory("astePos").up()
    if core.getKeyPressList("q"):
        core.memory("astePos").left()
    if core.getKeyPressList("d"):
        core.memory("astePos").right()




core.main(setup, run)
'''

import core
from math import *
from pygame.math import *
from random import *
from player import *
from pygame.time import *


def setup():
    core.fps = 30
    core.WINDOW_SIZE = [720, 720]
    core.memory('astePos', Player("J0", 360, 360, 0))
    core.memory("bobHistorique", [])
    # core.memory('origine', Vector2(250, 250))
    core.memory("incremental", Vector3(0, 0, 0))
    core.memory("projo", Projectile("K0", 360, 360))
    core.memory("p2", Vector2(0, 0))
    core.memory("test", Vector2(0, 0))
    core.memory("Vit", Vector2(0, 0))
    core.memory("incre", Vector2(0, 0))

def run():
    clock()
    touches()
    move()
    show()
    projectile()
    resetpos()


def clock():

    horlo = Clock()

    horlo.tick(30)
    if core.memory("incremental").x >= 120:
        core.memory("astePos").vitesse += core.memory("astePos").accel
        core.memory("incremental").x = 0
    core.memory("incremental").x += horlo.get_time()

def show():

    core.cleanScreen()
    p1 = Vector2(core.memory("astePos").position.x, core.memory("astePos").position.y) + Vector2(-5, 0).rotate(
        -90 - core.memory("astePos").position.z)

    p2 = Vector2(core.memory("astePos").position.x, core.memory("astePos").position.y) + Vector2(0, 15).rotate(
        -90 - core.memory("astePos").position.z)

    p3 = Vector2(core.memory("astePos").position.x, core.memory("astePos").position.y) + Vector2(5, 0).rotate(
        -90 - core.memory("astePos").position.z)

    core.Draw.polygon([255, 0, 0], (p1, p2, p3))
    core.memory("p2", p2)




def move():
    core.memory("astePos").position.xy += core.memory("astePos").vitesse.xy
    if core.memory("astePos").accel.xy == Vector2(0, 0):
        if core.memory("astePos").vitesse.x > 0:
            core.memory("astePos").vitesse.x -= 0.1
            if core.memory("astePos").vitesse.x < 0:
                core.memory("astePos").vitesse.x = 0
        elif core.memory("astePos").vitesse.x < 0:
            core.memory("astePos").vitesse.x += 0.1
            if core.memory("astePos").vitesse.x > 0:
                core.memory("astePos").vitesse.x = 0

        if core.memory("astePos").vitesse.y > 0:
            core.memory("astePos").vitesse.y -= 0.1
            if core.memory("astePos").vitesse.y < 0:
                core.memory("astePos").vitesse.y = 0
        elif core.memory("astePos").vitesse.y < 0:
            core.memory("astePos").vitesse.y += 0.1
            if core.memory("astePos").vitesse.y > 0:
                core.memory("astePos").vitesse.y = 0

'''
def shoot():
    core.memory("projo").shoot()


    if core.getKeyPressList("e"):
        core.memory("Vit").xy = core.memory("astePos").vitesse.xy

        if core.memory("test").x == 0:
            core.memory("test").x = 1
            core.memory("projo").pos.xy = core.memory("p2")
            core.memory("projo").pos.z = core.memory("astePos").position.z

        core.memory("test").x = 0
    core.memory("projo").pos.xy += core.memory("projo").vit.xy + core.memory("Vit")
    core.Draw.circle((0, 255, 0), (core.memory("projo").pos.x, core.memory("projo").pos.y), 2.5)
'''
def projectile():
    core.memory("projo").shoot()


    if core.getKeyPressList("e"):
        core.memory("Vit").xy = core.memory("astePos").vitesse.xy
        core.memory("incre").x += 1
        if core.memory("incre").x > 5:
            core.memory("incre").x = 0
        if core.memory("test").x == 0:
            core.memory("test").x = 1
            core.memory("projo").pos.xy = core.memory("p2")
            core.memory("projo").pos.z = core.memory("astePos").position.z
        core.memory("test").x = 0
    core.memory("projo").pos.xy += core.memory("projo").vit.xy + core.memory("Vit")
    if core.memory("incre").x >1:
        core.memory("projo").proj1()
    if core.memory("incre").x >2:
        core.memory("projo").proj2()
    if core.memory("incre").x >3:
        core.memory("projo").proj3()
    if core.memory("incre").x >4:
        core.memory("projo").proj4()
    if core.memory("incre").x == 5:
        core.memory("projo").proj5()


def resetpos():
    if core.memory("astePos").position.x > 720:
        core.memory("astePos").position.x = 0
    elif core.memory("astePos").position.x < 0:
        core.memory("astePos").position.x = 720
    if core.memory("astePos").position.y > 720:
        core.memory("astePos").position.y = 0
    elif core.memory("astePos").position.y < 0:
        core.memory("astePos").position.y = 720
    if core.memory("projo").pos.x > 720:
        core.memory("projo").pos.x = 0
    elif core.memory("projo").pos.x < 0:
        core.memory("projo").pos.x = 720
    if core.memory("projo").pos.y > 720:
        core.memory("projo").pos.y = 0
    elif core.memory("projo").pos.y < 0:
        core.memory("projo").pos.y = 720
def touches():
    core.memory("astePos").accel.xy = 0, 0
    if core.getKeyPressList("z"):
        core.memory("astePos").up()
    if core.getKeyPressList("d"):
        core.memory("astePos").left()
    if core.getKeyPressList("s"):
        core.memory("astePos").down()
    if core.getKeyPressList("q"):
        core.memory("astePos").right()



core.main(setup, run)
