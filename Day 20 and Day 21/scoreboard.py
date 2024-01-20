from turtle import Turtle

class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.scoreLeft = 0
            self.scoreRight = 0           
            self.color("white")
            self.penup()
            self.goto(0,260)
            self.write(f" {str(self.scoreLeft)} : {str(self.scoreRight)}", align="center", font=("Courier", 24, "normal"))
            self.hideturtle()
            self

        def increase_scoreLeft(self):
            self.scoreLeft += 1
            self.clear()
            self.write(f" {str(self.scoreLeft)} : {str(self.scoreRight)}", align="center", font=("Courier", 24, "normal"))

        def increase_scoreRight(self):
            self.scoreRight += 1
            self.clear()
            self.write(f" {str(self.scoreLeft)} : {str(self.scoreRight)}", align="center", font=("Courier", 24, "normal"))