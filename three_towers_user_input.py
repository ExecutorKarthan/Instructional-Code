import turtle

def get_brick_value():
    value = input("How many bricks high do you want your towers? ")  
    try:
        max_bricks = int(value)
        return max_bricks
    except:
        print("Error! You need to input a numeric integer or float. All other values will not work")
        get_brick_value()
        
def get_color_list():
    value = input("What colors do you want the towers to alternate? Seperate your selections with the ',' character. " + "\n") 
    color_list = value.split()
    reference_color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
    for color in color_list:
        valid_color = False
        for ref in reference_color_list:
            if(color == ref):
                valid_color = True
                break
        if(valid_color):
            continue
        else:
            print("Error! You need to input a list of valid colors, spelled correctly. All other values will not work")
            get_color_list()
            break
    return color_list
        

def make_brick(tower_num, brick, max_height, max_bricks, color_list):
    if(tower_num == 0):
        if(brick % 2 == 0):
            builder.fillcolor(color_list[0])
        if(brick % 2 == 1):
            builder.fillcolor(color_list[1])
    if(tower_num == 1):
        if(brick % 3 == 0):
            builder.fillcolor(color_list[0])
        if(brick % 3 == 1):
            builder.fillcolor(color_list[1])
        if(brick % 3 == 2):
            builder.fillcolor(color_list[2])
    if(tower_num == 2):
        if(brick % 4 == 0):
            builder.fillcolor(color_list[0])
        if(brick % 4 == 1):
            builder.fillcolor(color_list[1])
        if(brick % 4 == 2):
            builder.fillcolor(color_list[2])
        if(brick % 4 == 3):
            builder.fillcolor(color_list[3])
    builder.begin_fill()
    builder.setheading(0)
    builder.forward(50)
    builder.right(90)
    builder.forward(max_height/max_bricks)
    builder.right(90)
    builder.forward(50)
    builder.right(90)
    builder.forward(max_height/max_bricks)
    builder.end_fill()
    builder.penup()
    builder.forward(max_height/max_bricks)
    builder.pendown()
    
max_height = 800

max_bricks = get_brick_value()
color_list = get_color_list()
builder = turtle.Turtle()
builder.speed(0)

for tower in range (0, 3):
    if (tower == 0):
        builder.penup()
        builder.goto(-400, -400)
        builder.pendown()
        for brick in range(1, max_bricks+1):
            make_brick(tower, brick, max_height, max_bricks, color_list)
    if (tower == 1):
        builder.penup()
        builder.goto(0, -400)
        builder.pendown()
        for brick in range(1, max_bricks+1):
            make_brick(tower, brick, max_height, max_bricks, color_list)
    if (tower == 2):
        builder.penup()
        builder.goto(400, -400)
        builder.pendown()
        for brick in range(1, max_bricks+1):
            make_brick(tower, brick, max_height, max_bricks, color_list)
            
wn = turtle.Screen().mainloop()