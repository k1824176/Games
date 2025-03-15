#snake game!
import turtle
import time

delay=0.12

#setup screen

background = turtle.Screen()
background.bgcolor("grey")
background.setup(width=500, height=500)
background.title("Classic Snake game")
background.tracer(0) #turns off screen updates
#snake head
headstub=turtle.Turtle()
headstub.speed(0)
headstub.shape("turtle")
headstub.color("green")
headstub.penup()
headstub.goto(0,0)
headstub.direction="stop"

#functions
def go_up():
    headstub.direction="up"
def go_down():
    headstub.direction="down"
def go_left():
    headstub.direction="left"
def go_right():
    headstub.direction="right"









def move():
    if headstub.direction =="up":
        y = headstub.ycor()
        headstub.sety(y+20)

    if headstub.direction =="down":
        y = headstub.ycor()
        headstub.sety(y-20)

    if headstub.direction =="left":
        x = headstub.xcor()
        headstub.setx(x+20)

    if headstub.direction =="right":
        x = headstub.xcor()
        headstub.setx(x+20)
#keyboared bindings
background.onkeypress(go_up, "w")
background.onkeypress(go_down, "s")
background.onkeypress(go_right, "d")
background.onkeypress(go_left, "a")



#main gameloop
while True:
    background.update()
    
    move()
    time.sleep(delay)






background.mainloop()