

import turtle

bg=turtle.Screen()
bg.bgcolor("black")
bg.title("cookie stuff")
bg.setup(width=600, height=700)

bg.register_shape("trolls.gif")

troll=turtle.Turtle()
troll.shape("trolls.gif")
troll.speed(0)
troll.goto(0,0)

clicks = 0

pen=turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,200)
pen.write(f"Clicks: {clicks}", align="center", font=("Comfortaa", 36, "bold"))


def clicked(x,y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Comfortaa", 36, "bold"))

troll.onclick(clicked)

bg.mainloop()