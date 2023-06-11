import turtle
s=turtle.getscreen()
t=turtle.Turtle()
t.hideturtle()
t.speed(9)
def rectangle(l,b):
    t.begin_fill()
    t.pendown()
    t.forward(l)
    t.rt(90)
    t.fd(b)
    t.rt(90)
    t.fd(l)
    t.rt(90)
    t.fd(b)
    t.end_fill()
    t.hideturtle()

def hanger():
    t.bk(50)
    rectangle(100,10)
    t.home()
    t.pendown()
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(10)

def head():
    t.penup()
    t.goto(-50,190)
    t.rt(90)
    t.pendown()
    t.circle(20)

def body():
    t.penup()
    t.seth(-90)
    t.goto(-50,150)
    t.pendown()
    t.fd(100)

def rightarm():
    t.penup()
    t.seth(-45)
    t.goto(-50,140)
    t.pendown()
    t.fd(50)

def leftarm():
    t.penup()
    t.seth(-135)
    t.goto(-50,140)
    t.pendown()
    t.fd(50)
    

def rightleg():
    t.penup()
    t.seth(-45)
    t.goto(-50,50)
    t.pendown()
    t.fd(50)
    

def leftleg():
    t.penup()
    t.seth(-135)
    t.goto(-50,50)
    t.pendown()
    t.fd(50)

functions=[hanger,head,body,rightarm,leftarm,rightleg,leftleg]
def call_function(n):
    functions[n]()


if __name__=="__main__":
    for i in range(7):
        call_function(i)   
    



