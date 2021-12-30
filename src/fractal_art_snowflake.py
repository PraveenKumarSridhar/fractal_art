from turtle import *

# shape("dot")
bgcolor("black")
speed(0)

def snowflake_side(length,level):
    if level == 0:
        forward(length)
        return
    length /= 3.0
    snowflake_side(length,level-1)
    
    left(60)
    snowflake_side(length,level-1)
    right(120)
    snowflake_side(length,level-1)
    left(60)
    snowflake_side(length,level-1)


def create_snowflake(sides,length):
    for _ in range(sides):
        snowflake_side(length,sides)
        right(360/sides)

pen(pencolor="red",fillcolor="red")
begin_fill()
create_snowflake(4,200)
end_fill()

# right(45)
# forward(100)
pen(pencolor="red")
right(45)
forward(100)
pen(pencolor="cyan",fillcolor="cyan")
begin_fill()
create_snowflake(4,50)
end_fill()
pen(pencolor="red")
left(45)
forward(50)
pen(pencolor="cyan",fillcolor="cyan")
begin_fill()
create_snowflake(4,50)
end_fill()

# pen(pencolor="purple",fillcolor="cyan")
# begin_fill()
# left(180)
# create_snowflake(4,200)
# end_fill()

# left(45)
# pen(pencolor="black")
# forward(100)
# pen(pencolor="purple",fillcolor="orange")
# begin_fill()
# create_snowflake(4,200)
# end_fill()

mainloop() # so the turtle module does not end or close when the program runs



