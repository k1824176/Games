import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Graphics Boilerplate")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Create a turtle
t = turtle.Turtle()
t.shape("triangle")
t.color("black")
t.speed(1)

#trunk length
trunk = 50
branch = 1

#turtle start position
t.penup()
t.goto(0, -250)
t.setheading(90)

# draw trunk
t.color("brown")
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(trunk/branch)
    t.right(30)
    branch += 1




# Keep the window open until it is closed by the user
turtle.done()