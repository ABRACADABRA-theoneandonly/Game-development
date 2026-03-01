#Mountain Landscape-Draw a mountain landscape using polygons for mountains and circles for the sun. 
import pgzrun
import random
WIDTH = 600
HEIGHT = 600
def draw():
    screen.fill("light blue")
    screen.draw.filled_circle((500, 100), 50, color="yellow")
    screen.draw.line((50, 400), (200, 150), color="dark gray")
    screen.draw.line((200, 150), (350, 400), color="dark gray")
    screen.draw.line((200, 450), (350, 200), color="dark gray")
    screen.draw.line((350, 200), (500, 450), color="dark gray")
    screen.draw.filled_rect(Rect((0, 400), (600, 200)), color="green")
pgzrun.go()