import pgzrun
import random
WIDTH=600
HEIGHT=600
def draw():
    screen.fill("white")
    w=250
    h=200
    for i in range(100):
        rectangle=Rect((0,0),(w,h))
        rectangle.center=(300,300)
        screen.draw.rect(rectangle,"blue")
        w-=20
        h+=10
        
pgzrun.go()