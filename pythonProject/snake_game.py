#snake game using functional programming

import turtle
import time
import random

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('cyan')
screen.title('Snake Game')


def create_snake():
    screen.tracer(0)
    snake = []
    x, y = 0, 0
    for _ in range(3):
        s = turtle.Turtle()
        s.shape('square')
        s.penup()
        s.goto(x, y)
        s.color('white')
        snake.append(s)
        x, y = x - 20, y
    screen.update()
    return snake

def move(snake, speed):
    screen.listen()
    screen.tracer(0)
    for i in range(len(snake) - 1, 0, - 1):
        x, y = snake[i - 1].pos()
        snake[i].goto(x, y)

    screen.onkey(lambda: s[0].left(90), 'a')
    screen.onkey(lambda: s[0].right(90), 'd')
    snake[0].forward(20)
    time.sleep(speed)
    screen.update()

def is_valid(snake):
    pos = list(map(lambda x: x.pos(), snake))
    if sorted(pos) != sorted(list(set(pos))):
        return False
    for x, y in pos:
        if x > 280 or x < -280 or y > 280 or y < -280:
            return False
    return True

def generate_ball(snake):
    screen.tracer(0)
    x, y = random.randrange(-280, 280, 20), random.randrange(-280, 280, 20)
    pos = list(map(lambda x: x.pos(), snake))
    while (x, y) in pos:
        x, y = random.randint(-280, 280), random.randint(-280, 280)
    ball = turtle.Turtle()

    ball.penup()
    ball.shape('square')
    ball.color('white')
    ball.goto(x, y)
    screen.update()
    return ball



#execution
s = create_snake()
b = generate_ball(s)

# generate scoreboard
score = 0
bg = turtle.Turtle()
bg.hideturtle()
bg.speed('fastest')
bg.penup()
bg.goto(0, 250)
bg.write(f'Score : {score}', align= 'center', font=('Arial', 15, 'bold'))

speed = 0.1

while is_valid(s):
    move(s, speed)
    def increase():
        global speed
        speed = max(0.01, speed - 0.05)
    def decrease():
        global speed
        speed = min(0.5, speed + 0.05)

    screen.onkey(increase, 'w')
    screen.onkey(decrease, 's')

    if s[0].distance(b) < 20:
        score += 1
        prev = s[-1].pos()
        screen.tracer(0)
        b.goto(*prev)
        s.append(b)
        b = generate_ball(s)
        bg.clear()
        bg.write(f'Score : {score}', align='center', font=('Arial', 15, 'bold'))
        screen.update()
        move(s, 0.1)


screen.clear()
screen.bgcolor('cyan')
bg.write(f'Score : {score}', align='center', font=('Arial', 15, 'bold'))
bg.goto(0, 0)
bg.write(f'Game Ends\n Score: {score}', align= 'center', font=('Arial', 50, 'bold'))


screen.exitonclick()
