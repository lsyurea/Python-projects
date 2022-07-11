import turtle
import random

s = turtle.Screen()
s.colormode(255)
s.bgcolor('cyan')

#instantiate objects
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
bg = turtle.Turtle()
bg.speed('fastest')

obj = [t1, t2, t3, t4, t5]
options = list(range(1, 6))

start_pos = -600, 400
end_pos = 600, 400

#draw grid
pos = [(-600, 'green'), (600, 'red')]
for i, col in pos:
    bg.penup()
    bg.home()
    bg.pensize(5)
    bg.pencolor(col)
    bg.setpos(i, 600)
    bg.pendown()
    bg.right(90)
    bg.forward(1200)
    bg.penup()


bg.setpos(600, 600)


for i in obj:
    i.speed('fastest')
    i.penup()
    i.setpos(start_pos)
    r, g, b = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
    i.shape('turtle')
    i.shapesize(5)
    i.fillcolor(r, g, b)
    start_pos = start_pos[0], start_pos[1] - 200

res = s.numinput('Bet', f'Which turtle will win the race? {options} with 1 from the top')
if not res:
    s.exitonclick()

max_dist = -600
has_ans = False
ans = 0
bg.color('black')
style = ('Arial', 30, 'italic')

while obj:
    cur = random.choice(obj)
    cur.forward(10)
    max_dist = max(max_dist, cur.xcor())
    if cur.xcor() >= 600:
        if not has_ans:
            ans = obj.index(cur) + 1
            has_ans = True

        obj.remove(cur)

bg.hideturtle()
bg.home()

bg.write(f'Turtle {ans} wins!', font=style, align='center')
bg.setpos(0, -40)
if res != ans:
    print('Sorry! You made the wrong bet')
    bg.write(f'Turtle {int(res)} is not it', font= style, align= 'center')

else:
    print('Well done!')
    bg.write(f'Correct guess!', font=style, align='center')

s.exitonclick()