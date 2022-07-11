import turtle
import pandas


screen = turtle.Screen()
screen.setup(800, 600)
screen.title('U.S states game')
t = turtle.Turtle()
bg = turtle.Turtle()
bg.hideturtle()
bg.penup()
scr = []
img = 'blank_states_img.gif'


screen.addshape(img)
t.shape(img)

data = pandas.read_csv('50_states.csv')


while len(scr) < 50:
    ans = screen.textinput(f'{len(scr)} / 50 states guessed', "What's the state's name?").title()
    if ans == 'Exit':
        break
    if ans in data['state'].to_list() and ans not in scr:
        res = data[data['state'] == ans]
        x, y = int(res.x), int(res.y)
        bg.goto(x, y)
        bg.write(ans)
        scr.append(res.state.item())


res = data.state.to_list()
for i in scr:
    res.remove(i)

res = pandas.DataFrame(res)
res.to_csv('states_to_learn.csv')