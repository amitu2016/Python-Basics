import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

colours = ["blue", "red", "green", "yellow"]

for i in colours:
        print(i)
        pen.color(i)
        pen.forward(100)
        pen.right(90)

turtle.done()