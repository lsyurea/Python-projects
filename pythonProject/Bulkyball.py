
from turtle import Turtle, Screen
from random import randint
import math

screen = Screen()
screen.bgcolor('cyan')
screen.colormode(255)

def n_gon(n, c, size, *pos):
    t = Turtle()
    t.speed(10)
    t.penup()
    t.goto(*pos)
    t.pendown()
    t.pencolor(c)
    t.shape('blank')
    ext_angle = 360 / n
    t.setheading(0)
    for i in range(n):
        t.forward(size)
        t.right(ext_angle)

def bulkyball(size, *pos):
    for i in range(3, 11):
        color = ()
        for t in range(3):
            k = randint(1, 255)
            color += (k,)
        n_gon(i, color, size, *pos)
        screen.bgcolor(*color)

def art(n):
    #default width is 400 by 300
    w, h, angle = 50, 50, math.radians(360 / n)
    for i in range(n):
        angle += math.radians(360 / (n + i))
        w += 100 * math.cos(angle)
        h += 100 * math.sin(angle)

        bulkyball((1/ (i + 1)) * 100, w, h)


art(10)
screen.bgcolor('cyan')
screen.exitonclick()