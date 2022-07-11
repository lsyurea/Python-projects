import turtle
t = turtle.Turtle()
s = turtle.Screen()
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
forward = lambda: t.forward(10)
backward = lambda: t.backward(10)
left = lambda: t.left(10)
right = lambda: t.right(10)
s.listen()
s.onkey(clear, 'c')
s.onkeypress(forward, 'w')
s.onkeypress(backward, 's')
s.onkeypress(left, 'a')
s.onkeypress(right, 'd')

s.exitonclick()

