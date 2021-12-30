from turtle import *

# shape("turtle")
bgcolor("black")
speed(0)

def tree(size,levels,angle,n_color):
    pencolor(n_color)

    if levels == 0:
        color(n_color)
        dot(size)
        color(n_color)
        return
    
    forward(size)
    #draw right branch
    right(angle)
    tree(size*0.80, levels-1, angle, n_color)    

    #draw left branch
    left(angle*2)
    tree(size*0.80,levels-1, angle, n_color)

    right(angle) # middle
    backward(size)

left(90)
tree(60,7,60,"red")

left(180)
tree(60,7,60,"green")

left(90)
forward(120)
tree(60,7,60,"blue")
backward(120)

left(180)
forward(120)
tree(60,7,60,"yellow")
backward(120)

mainloop() # so the turtle module does not end or close when the program runs



