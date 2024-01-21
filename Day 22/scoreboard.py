from turtle import Turtle



class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.score = 0
            self.color("Black")
            self.penup()
            self.goto(-250,200)
            self.write(f"Level: {str(self.score)}", align="left", font=("Courier", 24, "normal"))
            self.hideturtle()
            self

        def increase_score(self):
            self.score +=1
            self.clear()
            self.write(f"Level:: {str(self.score)}", align="left", font=("Courier", 24, "normal"))


        def game_over(self):
            self.color("white")
            self.penup()
            self.goto(200,0)
            self.write("GAME OVER", align="center", font=("Courier", 40, ""))
