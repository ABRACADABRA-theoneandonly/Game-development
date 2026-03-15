import pgzrun
import random
WIDTH=400
HEIGHT=400
score=0
game_over=False
snowman=Actor("snowman")
gift=Actor("gift")
sun=Actor("sun")
gift.pos=(200,110)
sun.pos=(100,110)
def timer():
    global game_over
    game_over=True
def draw():
    screen.blit("snowbg",(0,0))
    snowman.draw()
    gift.draw()
    sun.draw()
    screen.draw.text("Score:"+str(score),(300,300))
    if game_over:
        screen.fill("black")
        screen.draw.text("Muahahaha you ded, you're score is "+str(score),(10,300))
def movement():
    gift.x=random.randint(50,350)
    gift.y=random.randint(50,350)
    sun.x=random.randint(70,330)
    sun.y=random.randint(70,330)
def update():
    global score,game_over
    if keyboard.w:
        snowman.y-=20
    if keyboard.a:
        snowman.x-=20
    if keyboard.s:
        snowman.y+=20
    if keyboard.d:
        snowman.x+=20
    gift_collected=snowman.colliderect(gift)
    if gift_collected:
        score+=10
        movement()
    if sun.colliderect(snowman):
        score-=10
        game_over=True
clock.schedule(timer,60.0)
pgzrun.go()