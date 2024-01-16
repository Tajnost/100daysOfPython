import turtle as t
import random



is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Turtle Race", prompt="Who will win? red, blue, green, or black? ")
print(user_bet)

colors = ["red", "blue", "green", "black", "yellow", "purple"]
y_position = [-100, -66, -33, 0, 33, 66, 100]
all_turtles = []

for turtle_index in range(len(colors)):
    timmy = t.Turtle(shape="turtle")
    timmy.penup()
    timmy.goto(-230,y_position[turtle_index])
    hello = timmy.color(colors[turtle_index])
    all_turtles.append(timmy)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            bla = screen.textinput(f"Race over!", f"{turtle.pencolor()} Won!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


