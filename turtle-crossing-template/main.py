import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('cyan')
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.up, 'w')
screen.onkeypress(player.down, 's')
screen.onkeypress(player.left, 'a')
screen.onkeypress(player.right, 'd')

c = CarManager()
s = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    c.create_cars()
    c.move_cars()
    screen.update()

    for car in c.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        c.increase_speed()
        s.to_update()
if not game_is_on:
    s.game_over()
screen.exitonclick()