import time
from turtle import Screen,Turtle
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "w")

score = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars(score)

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 280:
        score += 1
        scoreboard.increase_score()
        player.goto(STARTING_POSITION)


screen.exitonclick()


