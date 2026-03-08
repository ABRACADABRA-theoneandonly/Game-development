import pgzrun
import random
WIDTH=600
HEIGHT=600
score=0
game_over=False
pacman=Actor("pacman")
dot=Actor("dot")
dot.pos=(200,110)
def timerrrrrrrrrrrr():
    global game_over
    game_over=True
def draw():
    screen.blit("bg",(0,0))
    pacman.draw()
    dot.draw()
    screen.draw.text("Score:"+str(score),(300,300))
    if game_over:
        screen.fill("black")
        screen.draw.text("Muahahaha you ded, you're score is "+str(score),(200,300))
def movement():
    dot.x=random.randint(50,550)
    dot.y=random.randint(50,550)
def update():
    global score
    if keyboard.w:
        pacman.y-=20
    if keyboard.a:
        pacman.x-=20
    if keyboard.s:
        pacman.y+=20
    if keyboard.d:
        pacman.x+=20
    dot_collected=pacman.colliderect(dot)
    if dot_collected:
        movement()
        score+=10
clock.schedule(timerrrrrrrrrrrr,60.0)
pgzrun.go()