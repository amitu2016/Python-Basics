import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

colours = ["blue", "red", "green", "yellow"]

for i in range(4):
        pen.color(colours[i])
        pen.forward(100)
        pen.right(90)

turtle.done()