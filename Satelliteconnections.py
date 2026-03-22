import pgzrun
import random
from time import time
WIDTH=600
HEIGHT=600
starttime=0
endtime=0
totaltime=0
satlist=[]
connections=[]
nextsat=0
totalsat=10
def satsuperior():
    global starttime
    for i in range(totalsat):
        satsat=Actor("sat")
        satsat.pos=random.randint(70,530),random.randint(70,530)
        satlist.append(satsat)
    starttime=time()
def draw():
    global totaltime
    screen.blit("space",(0,0))
    n=1
    for i in satlist:
        screen.draw.text(str(n),(i.pos[0],i.pos[1]+20))
        i.draw()
        n+=1
    for i in connections:
        screen.draw.line(i[0],i[1],"white")
    if nextsat<totalsat:
        totaltime=time()-starttime
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=70)
    else:
        screen.draw.text(str(round(totaltime,1)),(10,10),fontsize=70)
def update():
    pass
def on_mouse_down(pos):
    global nextsat,connections
    if nextsat<totalsat:
        if satlist[nextsat].collidepoint(pos):
            if nextsat:
                connections.append((satlist[nextsat-1].pos,satlist[nextsat].pos))
            nextsat+=1
        else:
            connections=[]
            nextsat=0
satsuperior()
pgzrun.go()