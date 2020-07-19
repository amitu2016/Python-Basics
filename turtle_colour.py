import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

for i  in range(4):
        if i ==0:
            pen.color("blue")
        if i ==1:
            pen.color("red")
        if i ==2:
            pen.color("green")
        if i ==3:
            pen.color("yellow")

        pen.forward(100)
        pen.right(90)
turtle.done()
    
    