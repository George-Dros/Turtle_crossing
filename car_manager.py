from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        y = random.randint(-220, 220)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.setposition(300, y)
        self.penup()
        self.speed(STARTING_MOVE_DISTANCE)

    def move(self):
        self.forward(MOVE_INCREMENT)



