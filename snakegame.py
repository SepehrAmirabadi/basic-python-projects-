from SimpleGraphics import *
from random import randint
stop= False
fruity = randint(50,550)
fruitx = randint (50,750)
def renders():
    sx= 200
    sy = 300
    rect (sx,sy,20,20)
    ellipse (fruitx,fruity,30,30)

def playermouvment():
    key = getHeldKeys()
    sdir=0
    if "Up" in key :
        sdir = 1
    elif "Down" in key:
        sdir = 2
    elif "left" in key:
        sdir = 3
    elif "right" in key:
        sdir = 4

    if sdir == 1:
        sy+=1
    elif sdir == 2:
        sy1-=1
    elif sdir == 3:
        sx-=1
    elif sdir == 4:
        sx+=1

while (stop==False):
    playermouvment()
    renders()
    clear()
    update()
