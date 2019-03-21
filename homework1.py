
import turtle
ob = turtle.Turtle()
colors = ['red','purple','blue','green','orange','yellow']
ob.speed(200)
for x in range(360):
   ob.pencolor(colors[x % 6])
   ob.width(x / 100 + 1)
   ob.forward(x)
   ob.left(59)