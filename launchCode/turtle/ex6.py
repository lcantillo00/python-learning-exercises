import turtle
wn=turtle.Screen()
li=turtle.Turtle()
num_side=int(input("enter number of sides"))
length_side=int(input("enter length of sides"))
for i in range(num_side):
    li.forward(length_side)
    li.left(360/num_side)
wn.exitonclick()
