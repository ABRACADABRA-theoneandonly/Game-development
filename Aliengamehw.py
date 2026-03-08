#Homework: repeat the same steps but with a different moving logic and character image.
import pgzrun
from random import randint
WIDTH=700
HEIGHT=700
Alien=Actor("alien.png")
messaGEEEE=""
def draw():
    screen.fill("black")
    Alien.draw()
    screen.draw.text(messaGEEEE,(300,300))
def update():
    if keyboard.a:
        Alien.x-=20
    if keyboard.d:
        Alien.x+=20
    if keyboard.W:
        Alien.y-=20
    if keyboard.s:
        Alien.y+=20
def randommmmmmly():
    Alien.x=randint(100,WIDTH-100)
    Alien.y=randint(100,HEIGHT-100)
def on_mouse_down(pos):
    global messaGEEEE
    if Alien.collidepoint(pos):
        messaGEEEE="Keep going!"
        randommmmmmly()   
    else:
         messaGEEEE="Try again..." 
pgzrun.go()