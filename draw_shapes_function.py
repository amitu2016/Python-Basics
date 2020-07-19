import turtle

paper = turtle.Screen()
pen = turtle.Turtle()


def square(mycolor):
    pen.color(mycolor)
    for i in range(4):
            pen.fd(100)
            pen.right(90)

def circle(mycolor):
    pen.color(mycolor)
    for i in range(360):
            pen.fd(1)
            pen.right(1)
            
def anyshape(sides,mycolor):
    pen.color(mycolor)
    angle = 360/sides
    for i in range(sides):
            pen.fd(100)
            pen.right(angle)




square("red")
circle("blue")
anyshape(8,"green")
turtle.done()