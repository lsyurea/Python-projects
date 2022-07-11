from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f'Score : 0', align='center', font=FONT)

    def to_update(self):
        self.clear()
        self.score += 1
        self.write(f'Score : {self.score}', align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game over', align='center', font=FONT)