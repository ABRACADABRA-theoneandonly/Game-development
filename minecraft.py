import pgzrun
import random
WIDTH=600
HEIGHT=600
score=0
game_over=False
v=Actor("villager")
e=Actor("emerald")
p=Actor("pillager")
e.pos=(200,110)
p.pos=(500,510)
def timer():
    global game_over
    game_over=True
def draw():
    screen.blit("bgg",(0,0))
    v.draw()
    e.draw()
    p.draw()
    screen.draw.text("Score:"+str(score),(300,300))
    if game_over:
        screen.fill("dark red")
        screen.draw.text("DEAD, You're score is "+str(score),(10,300))
def movement():
    e.x=random.randint(50,350)
    e.y=random.randint(50,350)
    p.x=random.randint(70,330)
    p.y=random.randint(70,330)
def update():
    global score,game_over
    if keyboard.w:
        v.y-=10
    if keyboard.a:
        v.x-=10
    if keyboard.s:
        v.y+=10
    if keyboard.d:
        v.x+=10
    e_collected=v.colliderect(e)
    if e_collected:
        score+=10
        movement()
    if p.colliderect(v):
        score-=10
        game_over=True
clock.schedule(timer,60.0)
pgzrun.go()