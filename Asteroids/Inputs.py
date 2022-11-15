
import core
from math import *
from pygame.math import *
from random import *
from player import Player
from pygame.time import *


def setup():
    core.fps = 30
    core.WINDOW_SIZE = [720, 720]
    core.memory('astePos', Player("J0", 360, 360, 0))
    core.memory("bobHistorique", [])
    # core.memory('origine', Vector2(250, 250))
    core.memory("incremental", Vector2(0, 0))


def run():
    clock()
    touches()
    move()
    resetpos()
    show()


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


def resetpos():
    if core.memory("astePos").position.x > 720:
        core.memory("astePos").position.x = 0
    elif core.memory("astePos").position.x < 0:
        core.memory("astePos").position.x = 720
    if core.memory("astePos").position.y > 720:
        core.memory("astePos").position.y = 0
    elif core.memory("astePos").position.y < 0:
        core.memory("astePos").position.y = 720
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
