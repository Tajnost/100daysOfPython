import colorgram as cg
import turtle as t
from random import randrange

screen = t.Screen()
spot = t.Turtle()
spot.shape("circle")
spot.home()
t.colormode(255)

TURTLE_SIZE = 60


x_axis = screen.window_width()
y_axis = screen.window_height()
y_axis_minus = -y_axis / 2
y_axizz = y_axis / 2
print(y_axizz)
print(y_axis_minus)
spot.penup()


color_list = cg.extract("image.jpg", 30)
color_palette = []
for i in range(len(color_list)):
    r = color_list[i].rgb.r
    g = color_list[i].rgb.g
    b = color_list[i].rgb.b
    new_color = (r, g, b)
    color_palette.append(new_color)

spot.goto(TURTLE_SIZE / 2 - x_axis / 2, y_axis / 2 - TURTLE_SIZE / 2)
spot.speed(100)
while y_axizz > y_axis_minus:
    y_axizz -= 50
    y_axis -= 100
    print(spot.pos())
    while x_axis > 0:
        x_axis -= 100

        spot.color(color_palette[randrange(0, len(color_palette))])
        spot.stamp()
        spot.pendown()
        spot.forward(0)
        spot.penup()
        spot.forward(100)
    spot.home()
    x_axis = screen.window_width()
    spot.goto(TURTLE_SIZE / 2 - x_axis / 2, y_axis / 2 - TURTLE_SIZE / 2)


screen = t.mainloop()


