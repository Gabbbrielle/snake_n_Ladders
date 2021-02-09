from turtle import *
class Grid():

    def __init__(self):

        self.grid = Turtle()
        self.grid.ht()
        self.grid.penup()
        self.grid.shape('turtle')
        self.grid.speed('fastest')
        x = -350
        y = -350
        self.grid.goto(x, y)
        self.grid.pendown()
        self.draw()


    def draw(self):
        x = -350
        y = -350
        for rows in range(11):
            self.grid.forward(711)
            y = y + 71
            self.grid.penup()
            self.grid.goto(x, y)
            self.grid.pendown()
        self.grid.penup()
        y = y - 71
        self.grid.goto(x, y)
        self.grid.setheading(270)

        for column in range(11):
            self.grid.pendown()
            self.grid.forward(711)
            self.grid.penup()
            x = x + 71
            self.grid.goto(x, y)
        self.grid.ht()




