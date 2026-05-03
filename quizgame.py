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
    message=message+f"           m Q: {index} of {count}"
    screen.draw.textbox(message, mbox, color="black")
    screen.draw.textbox(str(timeleft),tbox,color="black")
    screen.draw.textbox("skip",sbox,color="black")
    screen.draw.textbox(question[0].strip(),qbox,color="black")
    i=1
    for j in boxes:
        screen.draw.textbox(question[i].strip(),j,color="black")
        i+=1
def update():
    movemessage()
def movemessage():
    mbox.x-=2
    if mbox.right<0:
        mbox.left=WIDTH
def readquestion():
    global count,questions
    file=open(filename,"r")
    for i in file:
        questions.append(i)
        count+=1
    file.close()
def readnextquestion():
    global index
    index+=1
    return questions.pop(0).split(",")
def on_mouse_down(pos):
    i=1
    for j in boxes:
        if j.collidepoint(pos):
            if i is int(question[5]):
                correctanswer()
            else:
                isgameover()
        i+=1
    if sbox.collidepoint(pos):
        skipquestion()
def correctanswer():
    global score,question,timeleft,questions
    score+=1
    if questions:
        question=readnextquestion()
        timeleft=10
    else:
        isgameover()
def isgameover():
    global question,timeleft,gameover
    msg=f"Game over u got: {score} questions correct"
    question=[msg,"-","-","-","-",5]
    timeleft=0
    gameover=True
def skipquestion():
    global question,timeleft
    if questions and not gameover:
        question=readnextquestion()
        timeleft=10
    else:
        isgameover()
def updatetime():
    global timeleft
    if timeleft:
        timeleft-=1
    else:
        isgameover()
readquestion()
question=readnextquestion()
clock.schedule_interval(updatetime,1)
pgzrun.go()