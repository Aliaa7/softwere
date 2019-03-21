import turtle
ob = turtle.Turtle()
ob.speed(10)
d=200
colors = ['red','purple','blue','yellow']
for i in range(1,200):

    ob.forward(d)
    ob.pencolor(colors[i % 4])
    ob.lt(90)

    d = d - 1
