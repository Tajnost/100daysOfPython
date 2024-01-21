from turtle import Turtle
import random as r
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_change = r.randint(1,6)
        if random_change == 2:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(r.choice(COLORS))
            random_y = r.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)


    def move_cars(self, score):
        for car in self.all_cars:
            hello = score * STARTING_MOVE_DISTANCE
            car.backward(hello)
            print(score)

