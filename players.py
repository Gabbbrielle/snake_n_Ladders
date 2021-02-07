import turtle
from turtle import *
import random
turtle.colormode(255)


class Player():
    def __init__(self):
        colors = [(138, 34, 179),(179, 34, 147),(179, 34, 75),(179, 66, 34),(179, 138, 34),(147, 179, 34)]
        self.player = Turtle()
        self.player.shape('turtle')
        self.player.color(random.choice(colors))
        self.player.speed('fastest')
        x = -350+(random.randint(10,60))
        y = -350+(random.randint(10,60))
        start_position = (x, y)
        self.player.penup()
        self.player.goto(start_position)
        self.player.setheading(random.randint(0, 300))

    def forward(self, distance):
        self.player.setheading(0)
        self.player.forward(distance)


