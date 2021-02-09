import turtle
from turtle import *
import random
turtle.colormode(255)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.player = Turtle()
        colors = [(138, 34, 179),(179, 34, 147),(179, 34, 75),(179, 66, 34),(179, 138, 34),(147, 179, 34)]
        self.player.shape('turtle')
        self.player.color(random.choice(colors))
        self.player.speed('fastest')
        x = -315+(random.randint(-10,10))
        y = -315+(random.randint(-10,10))
        start_position = (x, y)
        self.player.penup()
        self.player.goto(start_position)
        print(self.player.pos())


    def forward(self, distance):
        self.player.setheading(0)
        self.player.forward(distance)

    def pos(self):
        self.player.pos()


