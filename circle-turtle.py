import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า
tao.color('magenta')
turtle.bgcolor("orange")


def circle():
    '''ฟังก์ชันนี้เอาไว้วาดรูปวงกลมรูปที่ 1'''
    for i in range(4):
        tao.circle(100)
        tao.circle(-100)
        tao.rt(45)
       
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(-220,0)
circle()

t=tao.clone()

def circle2():
    '''ฟังก์ชันนี้เอาไว้วาดรูปวงกลมรูปที่ 2'''
    for i in range(4):
        t.circle(100)
        t.circle(-100)
        t.rt(45)

def Go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

Go(220,0)
circle2()
