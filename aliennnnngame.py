import pgzrun
from random import randint
WIDTH=700
HEIGHT=700
Alien=Actor("aliennnnnnnnnnnnnnnnnnn")
messaGEEEE=""
def draw():
    screen.fill("black")
    Alien.draw()
    screen.draw.text(messaGEEEE,(300,300))
def update():
    if keyboard.left:
        Alien.x-=20
    if keyboard.right:
        Alien.x+=20
    if keyboard.up:
        Alien.y-=20
    if keyboard.down:
        Alien.y+=20
def randommmmmmly():
    Alien.x=randint(80,WIDTH-80)
    Alien.y=randint(80,HEIGHT-80)
def on_mouse_down(pos):
    global messaGEEEE
    if Alien.collidepoint(pos):
        messaGEEEE="Keep going!"
        randommmmmmly()   
    else:
         messaGEEEE="Try again..." 
pgzrun.go()