
import turtle

def drawPoly(t, num_sides, side_length):
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360/num_sides)

wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color('hotpink')
tess.pensize(3)

drawPoly(tess, 8, 50)
