import turtle as t


class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10


    def movement(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.y_move *= -1
    
    def bouncePaddle(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0,0)


