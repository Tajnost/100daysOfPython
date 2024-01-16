import turtle as t

etchA = t.Turtle()
screen = t.Screen()


def moveFoward():
    etchA.forward(10)

def moveBackwar():
    etchA.backward(10)

def turnLeft():
    etchA.left(10)

def turnRight():
    etchA.right(10)





screen.listen()
screen.onkey(key="w", fun=moveFoward)
screen.onkey(key="s", fun=moveBackwar)
screen.onkey(key="a", fun=turnLeft)
screen.onkey(key="d", fun=turnRight)
screen.onkey(key="space", fun=t.resetscreen)
screen = t.mainloop()
