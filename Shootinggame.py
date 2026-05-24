import pgzrun
import random
WIDTH=600
HEIGHT=600
ship=Actor("spaceship")
ship.pos=(400,500)
blist=[]
for i in range(4):
    for j in range(4):
        blist.append(Actor("bee"))
        blist[-1].x=100+50*i
        blist[-1].y=80+50*j
bullets=[]
speed=5
score=0
direction=1
ship.dead=False
ship.countdown=90
def handle_gameover():
    screen.draw.text("GAME OVERRRRRRRRRRRRR",(300,300))
def update():
    global score,direction
    movedown=False
    if ship.dead==False:
        if keyboard.a:
            ship.x-=speed
            if ship.x<=0:
                ship.x=0
        if keyboard.d:
            ship.x+=speed
            if ship.x>=WIDTH:
                ship.x=WIDTH
    for i in bullets:
        if i.y<=0:
            bullets.remove(i)
        else:
            i.y-=10
    if len(blist)==0:
        handle_gameover()
    if len(blist)>0 and (blist[-1].x>WIDTH-80 or blist[0].x<80):
        movedown=True
        direction=direction*-1
    for i in blist:
        i.x+=5*direction
        if movedown==True:
            i.y+=100
        if i.y>HEIGHT:
            blist.remove(i)
        for j in bullets:
            if i.colliderect(j):
                score+=100
                blist.remove(i)
                bullets.remove(j)
                if len(blist)==0:
                    handle_gameover()
        if i.colliderect(ship):
            ship.dead=True
    if ship.dead:
        ship.countdown-=1
    if ship.countdown==0:
        ship.dead=False
        ship.countdown=90
def draw():
    screen.fill("light blue")
    ship.draw()
    for i in blist:
        i.draw()
    for i in bullets:
        i.draw()
    screen.draw.text("Score:"+str(score),(30,30))
    if len(blist)==0:
        handle_gameover()
def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50
pgzrun.go()