from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #keep track of high score
        with open('data.txt', 'r') as scr:
            self.high_score = int(scr.read())
        self.to_update = False
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.to_update:
            with open('data.txt', 'w') as scr:
                scr.write(str(self.score))

        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.to_update = True
            self.high_score = self.score
        self.clear()
        self.update_scoreboard()
