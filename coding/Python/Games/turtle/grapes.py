from operator import ne
import turtle
import os

#set up screen
wn=turtle.Screen()
wn.bgcolor("purple")
wn.title("1 2 3 pounds of poo on the bathroom floor")
#Dan is getting old. He is saying bad words here. Sigh, life is so fast

boarderdrawer=turtle.Turtle()
boarderdrawer.shape("classic")
boarderdrawer.speed(0)
boarderdrawer.color("yellow")
boarderdrawer.penup()
boarderdrawer.setposition(-225,-225)
boarderdrawer.pensize(5)
boarderdrawer.pendown()
for side in range(4):
    boarderdrawer.fd(450)
    boarderdrawer.lt(90)
boarderdrawer.hideturtle()

player=turtle.Turtle()
player.color("orange")
player.shape("classic")
player.penup()
player.speed(0)
player.setposition(0, -175)
player.setheading(90)

playerspeed=15

def move_left():
    x=player.xcor()
    x-=playerspeed
    if x < -200:
        x=-200
    player.setx(x)

def move_right():
    x=player.xcor()
    x +=playerspeed
    if x > 200:
        x = 200
    player.setx(x)






#keys
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
#Hi i am grapes the conquerer
grapes=turtle.Turtle()
grapes.color("grey")
grapes.shape("square")
grapes.penup()
grapes.setposition(0,175)
grapes.setheading(90)

grapesspeed=15

#main game loop
while True:
    x=grapes.xcor()
    x += grapesspeed
    grapes.setx(x)
delay=input("hi i love grapes aghhhhhhhhhh dead man mode")