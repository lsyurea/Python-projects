import turtle
import random
import math

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('cyan')
t.speed('fastest')
s.colormode(255)

def randomise_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return r, g, b

def three_dimension_circle(n):
    for i in range(n):
        t.color(randomise_color())
        t.circle(75)
        t.left(360/n)


def donut(n, radius):
    t.setheading(0)
    t.setpos(0, 0)
    a = 0
    for i in range(n):
        t.penup()
        t.goto(- radius * math.sin(math.radians(a)), 0 - radius + radius * math.cos(math.radians(a)))
        t.pendown()
        t.color(randomise_color())
        t.circle(75)
        a += 360/n




donut(100, 150)
# three_dimension_circle(50)


s.exitonclick()