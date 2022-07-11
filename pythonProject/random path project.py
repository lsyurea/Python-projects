import turtle
import random


t = turtle.Turtle()
t.speed(10)
t.pensize(10)
shapes_available = turtle.getshapes()
shape = random.choice(shapes_available)
t.shape(str(shape))


s = turtle.Screen()
s.colormode(255)
s.bgcolor('cyan')

def randomise_color():
    res = ()
    for _ in range(3):
        u = random.randint(1, 255)
        res += (u,)
    return res

#width = 400 pixels, height = 300 pixels
for i in range(40):
    t.pencolor(*randomise_color())
    c = random.randint(1, 2)
    if c == 1:
        t.left(90)
    else:
        t.right(90)
    cur = t.heading()
    t.forward(random.choice([50, 100]))


s.exitonclick()