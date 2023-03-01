# The Authors of this code are Saerin Bong and Olivia Busk

import turtle
riley=turtle.Turtle()
riley.width(5)
riley.speed(0)

def draw_star(color):
    for side in range(5):
        riley.forward(100)
        riley.right(144)
        riley.color(color)

mood=input("what mood are you in? ")
if mood=="happy":
    draw_star("pink")
if mood=="sad":
    draw_star("blue")
elif mood=="sleepy":
    draw_star("green")
else:
    draw_star("red")
