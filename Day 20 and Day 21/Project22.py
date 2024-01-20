import turtle as t
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)


l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

scoreRight=0
igra_on = True
while igra_on:
    screen.update()
    ball.movement()
    sleep(0.1)

    #Detecing collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    ## Detect Col z desno iun levo    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() > -330:
        ball.bouncePaddle()

    
    if ball.xcor() > 400:
        scoreboard.increase_scoreLeft()
        ball.reset()
    
    if ball.xcor()< -400:
        scoreboard.increase_scoreRight()
        ball.reset()
















screen.exitonclick()