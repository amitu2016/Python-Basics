import turtle

paper = turtle.Screen()
pen = turtle.Turtle()

while True:
        sides = int(input("How many sides you want to draw ? "))
        print(f"Sides are {sides}")

        mycolors = []

        for i in range(sides):
                colour = input("Give a colour ")
                mycolors.append(colour)
                print(mycolors)

        for i in range(sides):
                pen.color(mycolors[i])
                pen.fd(100)
                pen.right(360/sides)


turtle.done()