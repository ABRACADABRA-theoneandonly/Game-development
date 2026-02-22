import pgzrun
import random
WIDTH=600
HEIGHT=600
def draw():
    screen.fill("white")
    w=200
    for i in range(100):
      screen.draw.filled_circle((300,300),w,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
      w-=20
pgzrun.go()