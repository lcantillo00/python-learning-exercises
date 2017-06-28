import turtle
screen = turtle.Screen()
screen.bgcolor ('limegreen')
mark = turtle.Turtle()
mark.shape('turtle')
mark.color('blue')

turns = 12

for i in range(turns):
    mark.penup()
    mark.forward(80)
    mark.pendown()
    mark.forward(10)
    mark.penup()
    mark.forward(10)
    mark.stamp()
    mark.backward(100)
    mark.left(360/turns)
