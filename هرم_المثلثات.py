import turtle as tr
x = tr.Turtle()
x.color("black")
x.speed(90)
ln = 10

def tri(l):
    x.begin_fill()
    x.fd(l)
    x.left(120)
    x.fd(l)
    x.left(120)
    x.fd(l)
    x.left(120)
    x.end_fill()



def stri():
    tri(ln)
    x.left(60)
    x.fd(ln)
    x.right(60)
    tri(ln)
    x.right(60)
    x.fd(ln)
    x.left(60)
    tri(ln)
    x.fd(ln)

def bigtri():
    stri()
    x.left(120)
    x.fd(ln*2)
    x.right(120)
    stri()
    x.backward(ln*2)
    x.right(60)
    x.fd(ln*2)
    x.left(60)
    stri()


def btri():
    bigtri()
    x.left(120)
    x.fd(ln*4)
    x.right(120)
    bigtri()
    x.backward(ln*4)
    x.right(60)
    x.fd(ln*4)
    x.left(60)
    bigtri()

def finaltri():
    btri()
    x.left(120)
    x.fd(ln*8)
    x.right(120)
    btri()
    x.backward(ln*8)
    x.right(60)
    x.fd(ln*8)
    x.left(60)
    btri()
finaltri()

def li():
    x.fd(2)
    x.left(1)

def leaf():
    for i in range(50):
        li()
    x.left(130)
    for i in range(50):
        li()
    x.left(125)

def flower():
    for i in range(10):
        leaf()
        x.left(40)
#flower()

tr.done()