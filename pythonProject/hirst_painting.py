#extracting colour from hirst_painting.jpg
import colorgram
import random
import turtle

c = colorgram.extract('hirst_painting.jpg', 30)
rgb_color = list(map(lambda x: (x.rgb.r, x.rgb.g, x.rgb.b), c))
rgb_color = list(filter(lambda x: x[0] <= 240 and x[1] <= 240 and x[2] <= 240, rgb_color))
t = turtle.Turtle()
t.hideturtle()
t.speed('fastest')
s = turtle.Screen()
s.colormode(255)
t.penup()
t.setpos(-250, - 250)
for k in range(10):
    for i in range(10):
        t.pendown()
        t.dot(20, random.choice(rgb_color))
        t.penup()
        t.forward(50)
    for j in range(2):
        if k % 2:
            t.right(90)
        else:
            t.left(90)
        t.forward(50)


s.exitonclick()