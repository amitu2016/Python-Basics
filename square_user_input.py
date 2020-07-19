import turtle

paper = turtle.Screen()
pen = turtle.Turtle()


while True:
        mycolour = input("Please Choose your colour ")

        pen.color(mycolour)

        for i in range(4):
                pen.forward(100)
                pen.right(90)

turtle.done()