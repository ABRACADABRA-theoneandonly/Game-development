import pgzrun
import random
WIDTH=600
HEIGHT=600
def draw():
    screen.fill("white")
    for i in range(100):
        screen.draw.line((300,0),(300,600),color="green")
    screen.draw.text("HELLOOOOOOOOOOOOOOOOO",(0,300),color="purple",fontsize=100)
pgzrun.go()