import pgzrun
WIDTH=600
HEIGHT=480
mbox=Rect(0,0,550,80)
qbox=Rect(0,0,440,96)
abox=Rect(0,0,200,100)
abox1=Rect(0,0,200,100)
abox2=Rect(0,0,200,100)
abox3=Rect(0,0,200,100)
tbox=Rect(0,0,100,96)
sbox=Rect(0,0,100,220)
score=0
timeleft=10
filename="questions.txt"
message=""
gameover= False
boxes=[abox,abox1,abox2,abox3]
questions=[]
count=0
index=0
mbox.move_ip(20,0)
qbox.move_ip(20,100)
abox.move_ip(30,220)
abox1.move_ip(250,220)
abox2.move_ip(30,340)
abox3.move_ip(250,340)
tbox.move_ip(480,100)
sbox.move_ip(480,220)
def draw():
    global message
    screen.clear()
    screen.fill("light blue")
    screen.draw.filled_rect(mbox,"dark blue")
    screen.draw.filled_rect(qbox,"dark blue")
    for i in boxes:
        screen.draw.filled_rect(i,"purple")
    screen.draw.filled_rect(tbox,"dark blue")
    screen.draw.filled_rect(sbox,"dark blue")
    message="Welcome to Quiz Master"
    message=message+f"         Q: {index} of {count}"
    screen.draw.textbox(message, mbox, color="black")
pgzrun.go()