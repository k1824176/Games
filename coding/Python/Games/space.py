#This is Albert. Daddy not allowed
import turtle
import os
dd=turtle.Screen()
dd.setup(800,500)
dd.bgcolor("black")
dd.title("Avengers Assemble")
#set up boundary you blockhead
bd_pen=turtle.Turtle()
bd_pen.speed(0)
bd_pen.color("purple")
bd_pen.penup()
bd_pen.setposition(-200,-200)
bd_pen.pendown()
bd_pen.pensize(3)
for mom in range(4):
    bd_pen.fd(400)
    bd_pen.lt(90)
bd_pen.hideturtle()
#create player turtle you..whats wrong with you,stupido
albert=turtle.Turtle()
albert.color("white") 
albert.penup()
albert.speed(0)
albert.shape("circle")
albert.setposition(0,-190)
#move the albert you dumbhead
albertspeed=18
def move(dir):
    x=albert.xcor()
    x = x + dir*albertspeed
    if x<-190:
        x=-190
    if x>190:
        x=190
    albert.setx(x)
def move_left():
    move(-1)
def move_right():
    move(1)
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
#where is the enemy, you stupido?!?!?

hi=turtle.Turtle()
hi.color("red")
hi.shape("triangle")
hi.penup()
hi.speed(0)
hi.setposition(-150,150)
hi.setheading(90)
hispeed=2
#where is the weapon, you blockhead?
gun=turtle.Turtle()
gun.color("green")
gun.shape("classic")
gun.penup()
gun.speed(0)
gun.setheading(90)
gun.shapesize(1,1)
gun.hideturtle()
gunspeed=10
#make the gun firable
#ready the gun! FIRE!!!
gunstate= "ready"
def fire_gun():
    global gunstate
    if gunstate=="ready":
        gunstate="fire"
        # move the bullet just above the player
        x=albert.xcor()
        y=albert.ycor() +10
        gun.setposition(x,y)
        gun.showturtle()

turtle.listen()
turtle.onkey(fire_gun,"space")
#Good job.Now we need a main game loop.NOW!
while True:
    x = hi.xcor()
    x += hispeed
    hi.setx(x)

    #move the enemy
    if hi.xcor() > 190:
        y = hi.ycor()
        y -= 15
        hispeed *= -1
        hi.sety(y)

    if hi.xcor() < -190:
        y = hi.ycor()
        y -= 15
        hispeed *= -1
        hi.sety(y)
    y=gun.ycor()
    y +=gunspeed
    gun.sety(y)
#Boarder checkin
    
        
delay=input("hi")
