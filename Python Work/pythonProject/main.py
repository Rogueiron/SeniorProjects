import turtle
import random
from turtle import Screen
screen = Screen()
canvas = screen.getcanvas()
iswhite = False


def main():
    turtle.hideturtle()
    turtle.bgcolor("Black")
    turtle.pencolor("Grey")
    screen.setup(2000, 1000)
    turtle.setx(950)
    turtle.setx(-950)
    rotation = 0
    rng = random
    go = "go"
    turtle.speed(500)
    percent = 5
    while go == "go":
        if turtle.xcor() >= 1000:
            go = "Stop"
        turtle.pensize(3)
        if rng.randint(1, 100)/100 * 10 <= percent:
            if rotation != 45:
                percent -= .25
                turtle.pencolor("Green")
                if rotation == -45:
                    turtle.left(90)
                    turtle.forward(amount())
                    rotation = 45
                elif rotation == 0:
                    turtle.left(45)
                    turtle.forward(amount())
                    rotation = 45
            elif rotation == 45:
                percent -= .25
                turtle.pencolor("Green")
                turtle.forward(amount())
        else:
            if rotation != -45:
                percent += .25
                turtle.pencolor("Red")
                if rotation == 45:
                    turtle.right(90)
                    turtle.forward(amount())
                    rotation = -45
                elif rotation == 0:
                    turtle.right(45)
                    turtle.forward(amount())
                    rotation = -45
            elif rotation == -45:
                percent += .25
                turtle.pencolor("Red")
                turtle.forward(amount())
    turtle.penup()
    percent2 = round(abs(turtle.ycor()/5), 2)
    if turtle.ycor() <= 0:
        turtle.setx(0)
        turtle.sety(0)
        turtle.pendown()
        turtle.color("Red")
        turtle.write("Down Wins By: " + str(percent2) + "%", move=True, align='center', font=('Arial', 100, 'normal'))
    elif turtle.ycor() >= 0:
        turtle.setx(0)
        turtle.sety(0)
        turtle.pendown()
        turtle.color("Green")
        turtle.write("Up Wins By: " + str(percent2) + "%", move=True, align='center', font=('Arial', 100, 'normal'))
    elif turtle.ycor() == 0:
        print("Tie")
    turtle.done()


def amount():
    funny = random.randint(1, 21)
    timer = 2
    if funny >= 21:
        global iswhite
        if iswhite == True:
            turtle.bgcolor("white")
            iswhite = False
        else:
            turtle.bgcolor("black")
            iswhite = True
        turtle.speed(500)
        return 100
    else:
        return funny


main()