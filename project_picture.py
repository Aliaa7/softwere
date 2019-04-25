import turtle
a=turtle.Turtle()
a.getscreen().bgcolor("black")
turtle.speed(0)
a.penup()
a.goto((-200,100))
a.pendown()
turtle.color("white","#f269d3")

def star(size):
    if size<=10 :
        return
    else:

        for i in range(5):
            turtle.begin_fill()
            turtle.fd(size)
            star(size/3)
            turtle.left(216)
            turtle.end_fill()
            turtle.stamp()
            turtle.ht()

star(360)
#turtle.pos()
#turtle.done()
a.penup()
a.goto((-500,0))
a.pendown()


colors= [ '#f269d3', '#d9f549','#d10e37', 'black', '#a295a7','#50a9e7']
for i in range(200):
    a.pencolor(colors[i % 6])
    a.fd(i)
    a.left(45)
    a.fd(100)
    a.left(175)
    a.fd(i)
turtle.done()

