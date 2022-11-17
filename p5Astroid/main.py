import random
import time

from pygame import Rect
from pygame.math import Vector2

import core
from prototype.draw import drawPlayer



def setup():
    core.fps = 30
    core.WINDOW_SIZE = [800, 800]

    core.memory("position", Vector2(400,400))
    core.memory('vitesse' , Vector2(0,-1))

    core.memory('projectiles', [])
    core.memory("target",Rect(random.randint(50,750),random.randint(50,750),50,50))

    core.memory('score', 0)

def creationProjectile():
    p = Vector2(core.memory("position"))
    v = Vector2(core.memory("vitesse"))
    v.scale_to_length(core.memory("vitesse").length() + 10)
    r = 10
    c = (255, 255, 255)
    startTime = time.time()

    proj = {"position": p, "vitesse": v, "rayon": r, 'startTime': startTime, "color": c}
    core.memory("projectiles").append(proj)



def run():
    core.cleanScreen()
    #print("nb projectiles : ", len(core.memory("projectiles")))

    #CLEAN
    for proj in core.memory('projectiles'):
        if time.time() - proj["startTime"] > 1.5:
            core.memory('projectiles').remove(proj)

    #Control
    if core.getKeyPressList("z"):
        core.memory('vitesse').scale_to_length(core.memory('vitesse').length() + 1)
    if core.getKeyPressList('d'):
        core.memory("vitesse", core.memory('vitesse').rotate(5))
    if core.getKeyPressList('q'):
        core.memory("vitesse", core.memory('vitesse').rotate(-5))


    #TIR
    if core.getKeyPressList("SPACE"):
        if len(core.memory("projectiles")) == 0:
            creationProjectile()
        else:
            if time.time() - core.memory("projectiles")[-1]["startTime"] > 0.5:
                creationProjectile()

    #DEPLACEMENT
    core.memory('position',  core.memory('position')+core.memory('vitesse') )

    for proj in core.memory("projectiles"):
        proj["position"] = proj["position"]+proj["vitesse"]


    #DESSIN TIR
    for proj in core.memory("projectiles"):
        core.Draw.circle(proj["color"],proj["position"],proj["rayon"])

    #Dessin Target
    core.Draw.rect((255,0,0),core.memory("target"))

    #Collision
    for proj in core.memory("projectiles"):
        if core.memory('target').collidepoint(proj["position"].x, proj["position"].y) :
            print("BOOM")
            core.memory("projectiles").remove(proj)
            core.memory("target", Rect(random.randint(50, 750), random.randint(50, 750), 50, 50))
            core.memory('score',core.memory('score')+1)



    core.Draw.text((255,255,255), "score : "+str(core.memory("score")) , (10,10),10,'')



    drawPlayer()








core.main(setup, run)
