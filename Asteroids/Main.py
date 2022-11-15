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
'''

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


'''def move():

    vel = Vector2(0, 1)
    angle = (vel.angle_to(Vector2(0, 1)) + core.memory("astePos").z) % 360
    core.memory("astePos").x += vel.x
    core.memory("astePos").y += vel.y
'''


def touches():
    if core.getKeyPressList("z"):
        core.memory("astePos").up()
    if core.getKeyPressList("q"):
        core.memory("astePos").left()
    if core.getKeyPressList("d"):
        core.memory("astePos").right()





core.main(setup, run)
