import turtle

def make_box(turtle):
    turtle.forward(50)
    turtle.left(90)

main = turtle
bob = turtle.Turtle()

for val in range(0, 4):
    make_box(bob)

turtle.mainloop()