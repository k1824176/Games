import turtle

asdf=turtle.Screen()
asdf.title("pong")
asdf.bgcolor("black")
asdf.tracer(0)
asdf.setup(width=600, height=400)

#player one
aa=turtle.Turtle()
aa.speed(0)
aa.shapesize(stretch_wid=5,stretch_len=1)
aa.shape("square")
aa.color("white")
aa.penup()
aa.goto(-250,0)
#player two
bb=turtle.Turtle()
bb.speed(0)
bb.shapesize(stretch_wid=5,stretch_len=1)
bb.shape("square")
bb.color("white")
bb.penup()
bb.goto(250,0)

Score1 = 0
Score2 = 0

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.xd=0.3
ball.yd=0.3


#pen
pen=turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,0)
pen.write(f"{Score1} : {Score2}", align="center", font=("Comfortaa", 36, "bold"))


#functions
def aamoveup():
    y = aa.ycor()
    aa.sety(y+20)

def aamovedown():
    y = aa.ycor()
    aa.sety(y-20)

def bbmoveup():
    y = bb.ycor()
    bb.sety(y+20)

def bbmovedown():
    y = bb.ycor()
    bb.sety(y-20)

#binding keyboard
asdf.listen()
asdf.onkeypress(aamoveup, "w")
asdf.onkeypress(aamovedown, "s")
asdf.onkeypress(bbmoveup, "Up")
asdf.onkeypress(bbmovedown, "Down")

#main game loop
while True:
    asdf.update()

    #ball movement
    ball.setx(ball.xcor() + ball.xd)
    ball.sety(ball.ycor() + ball.yd)

    #Border checking
    if ball.ycor() > 190:
        ball.sety(190)
        ball.yd *= -1
    
    if ball.ycor() < -190:
        ball.sety(-190)
        ball.yd *= -1

    if ball.xcor() > 290:
        pen.clear()
        Score1 += 1
        pen.write(f"{Score1} : {Score2}", align="center", font=("Comfortaa", 36, "bold"))
        ball.goto(0,0)
        ball.xd *= -1

    if ball.xcor() < -290:
        pen.clear()
        Score2 += 1
        pen.write(f"{Score1} : {Score2}", align="center", font=("Comfortaa", 36, "bold"))
        ball.goto(0,0)
        ball.xd *= -1

    #paddle and ball collisions
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < bb.ycor() + 40 and ball.ycor() > bb.ycor() -40):
        ball.setx(240)
        ball.xd *= -1
    
    if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < aa.ycor() + 40 and ball.ycor() > aa.ycor() -40):
        ball.setx(-240)
        ball.xd *= -1

