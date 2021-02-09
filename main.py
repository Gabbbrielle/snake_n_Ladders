# 8 - Write a function that will play a rubbish version of the board game snakes and ladders (https://
# en.wikipedia.org/wiki/Snakes_and_Ladders). In this game, two players compete to get from
# square 1 to square 100. Players take alternative turns, and move between 1 and 6 spaces based
# on a random roll of the dice. If they land on a square that ends in 5 (e.g. 5,
# 15, 25, etc.), they land on a ladder and move forward 9 spaces. If they land on a square that ends
# in 0 (e.g. 10, 20, 30, etc.), they land on a snake and go back to the start. The game will be
# explained using text commentary that you should print to the screen.

from turtle import *
from grid import Grid
from players import Player
import random
import time
import datetime
clock = datetime.datetime.now()
screen = Screen()
screen.setup(width=850, height=850, startx=300, starty=0)
screen.screensize(800, 800)
def coordinates():
    """returns the coordinates for each
 square's center starting from the bottom left to top right"""
    position = []
    x = -315
    y = -315
    for row in range(10):
        for column in range(10):
            position.append((x,y))
            x = x + 71
        y = y +71
        x = -315
    return position
positions = coordinates()
print(positions)
print(len(positions))
dice = random.randint(1, 6)
screen.title('Snake and Ladders')
grid = Grid()
player1 = Player()
player2 = Player()

for turns in range(9):
    for player in (player1, player2):
        player.forward(71)
        print(player.pos())
        time.sleep(1)









screen.exitonclick()
