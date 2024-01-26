import turtle
import random

def change_shape(turtle):
    rand_shape = ["square", "circle", "triangle", "turtle"]
    shape = rand_shape[random.randint(0, 3)]
    turtle.shape(shape)

def make_ring(turtle, x_cor, y_cor, color):
    change_shape(turtle)
    turtle.color(color)
    turtle.penup()
    turtle.goto(x_cor, y_cor)
    turtle.pendown()
    turtle.circle(50)
    

leo = turtle.Turtle()
leo.width(15)

rings = ["blue", "black", "green", "purple", "yellow"]
x_cor = -50
y_cor = -50

for color in rings:
    make_ring(leo, x_cor, y_cor, color)
    x_cor = x_cor + 20
    y_cor = y_cor + 20

wn = turtle.Screen()

wn.mainloop()

