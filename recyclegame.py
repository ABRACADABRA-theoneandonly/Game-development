import pgzrun
import random
HEIGHT=600
WIDTH=800
levels=10
fartspeed=10
itemslist=["battery","chips","corn","baby"]
gameover=False
gamecomplete= False
currentlevel=1
items=[]
animations=[]
def draw():
    global items
    screen.clear()
    screen.blit("bgd",(0,0))
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
    itemstocreate=["bottle"]
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