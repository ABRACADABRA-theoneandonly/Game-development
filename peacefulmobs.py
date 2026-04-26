import pgzrun
import random
HEIGHT=600
WIDTH=600
levels=10
startspeed=10
itemslist=["enderdragon","witherstorm","zombie","pillager"]
game_over=False
game_complete= False
currentlevel=1
items=[]
animations=[]
def draw():
    global items
    screen.clear()
    screen.blit("bgg",(0,0))
    if game_over:
        screen.draw.text("YOU LOST",fontsize=30,center=(400,300),color="dark red")
    elif game_complete:
        screen.draw.text("YOU WON",fontsize=30,center=(400,300),color="dark green")
    else:
        for i in items:
            i.draw()
def update():
    global items
    if len(items)==0:
        items=make_items(currentlevel)
def make_items(extraitems):
    itemstocreate=optiontocreate(extraitems)
    newitems=createitems(itemstocreate)
    layoutitems(newitems)
    animateitems(newitems)
    return newitems
def optiontocreate(extraitems):
    itemstocreate=["villager"]
    for i in range(0,extraitems):
        randomoption=random.choice(itemslist)
        itemstocreate.append(randomoption)
    return itemstocreate
def createitems(itemstocreate):
    newitems=[]
    for i in itemstocreate:
        item=Actor(i)
        newitems.append(item)
    return newitems
def layoutitems(itemstolayout):
    gaps=len(itemstolayout)+1
    gapsize=WIDTH/gaps
    random.shuffle(itemstolayout)
    for i,j in enumerate(itemstolayout):
        newx=(i+1)*gapsize
        j.x=newx
def animateitems(itemstoanimate):
    global animations
    for i in itemstoanimate:
        duration=startspeed-currentlevel
        i.anchor=("center","bottom")
        animation=animate(i,duration=duration,on_finished=handlegame_over,y=HEIGHT)
        animations.append (animation)
def handlegame_over():
    global game_over
    game_over= True
def on_mouse_down(pos):
    global items, currentlevel
    for i in items:
        if i.collidepoint(pos):
            if "villager" in i.image:
                handlegame_complete()
            else:
                handlegame_over()
def handlegame_complete():
    global currentlevel, items, animations, game_complete
    stop_animations(animations)
    if currentlevel==levels:
        game_complete=True
    else:
        currentlevel+=1
        items=[]
        animations=[]
def stop_animations(animationstostop):
    for i in animationstostop:
        if i.running:
            i.stop()
pgzrun.go()