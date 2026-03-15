import pgzrun
import random
WIDTH=600
HEIGHT=600
satlist=[]
connections=[]
nextsat=0
totalsat=10
def satsuperior():
    for i in range(totalsat):
        satsat=Actor("sat")
        satsat.pos=random.randint(70,530),random.randint(70,530)
        satlist.append(satsat)
def draw():
    screen.blit("space",(0,0))
    n=1
    for i in satlist:
        screen.draw.text(str(n),(i.pos[0],i.pos[1]+20))
        i.draw()
        n+=1
satsuperior()
pgzrun.go()