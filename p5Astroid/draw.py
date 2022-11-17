from pygame.math import Vector2

import core


def drawPlayer():
    vectP1 = core.memory("vitesse")
    vectP1 = vectP1.rotate(90)
    vectP1.scale_to_length(10)
    P1 = core.memory("position") + vectP1

    vectP2 = Vector2(core.memory("vitesse"))
    vectP2.scale_to_length(40)
    P2 = core.memory("position") + vectP2

    vectP3 = core.memory("vitesse")
    vectP3 = vectP3.rotate(-90)
    vectP3.scale_to_length(10)
    P3 = core.memory("position") + vectP3

    core.Draw.polygon((255, 0, 0), (P1, P2, P3))
