starting_position=(0,-280)
move_distance=10
finish_line=280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.left(90)
        self.goto(starting_position)
    def up(self):
        self.forward(move_distance)
    def finishing(self):
        if self.ycor()==finish_line:
            self.goto(starting_position)
            self.clear()