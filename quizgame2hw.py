import pgzrun
WIDTH=600
HEIGHT=480
mbox=Rect(0,0,550,80)
qbox=Rect(0,0,440,96)
abox=Rect(0,0,150,100)
abox1=Rect(0,0,150,100)
abox2=Rect(0,0,150,100)
abox3=Rect(0,0,150,100)
tbox=Rect(0,0,100,96)
sbox=Rect(0,0,100,220)
score=0
timeleft=10
filename="questions2.txt"
message=""
gameover= False
boxes=[abox,abox1,abox2,abox3]
questions=[]
count=0
index=0
mbox.move_ip(20,0)
qbox.move_ip(20,100)
abox.move_ip(60,220)
abox1.move_ip(290,220)
abox2.move_ip(60,340)
abox3.move_ip(290,340)
tbox.move_ip(480,100)
sbox.move_ip(480,220)
def draw():
    global message
    screen.clear()
    screen.fill("black")
    screen.draw.filled_rect(mbox,"dark green")
    screen.draw.filled_rect(qbox,"dark green")
    for i in boxes:
        screen.draw.filled_rect(i,"green")
    screen.draw.filled_rect(tbox,"dark green")
    screen.draw.filled_rect(sbox,"dark green")
    message="Welcome to Quiz Master"
    message=message+f"           m Q: {index} of {count}"
    screen.draw.textbox(message, mbox, color="white")
pgzrun.go()