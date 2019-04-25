import turtle
a=turtle.Turtle()
a.speed(1000)
colors= [ '#f269d3', '#d9f549','#d10e37', 'black', '#a295a7','#50a9e7']
for i in range(200):
    a.pencolor(colors[i % 6])
    a.fd(100)
    a.left(45)
    a.fd(100)
    a.left(90)
    a.fd(100)
    a.left(45)
    a.fd(100)
    a.left(1)

turtle.done()