Font=("courier",24,"normal")
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("Black")
        self.penup()
        self.goto(-280,250)
        self.write(f"level : {self.level}",align="left",font=Font)
        self.hideturtle()
    def update(self):
        self.write(f"level : {self.level}",align="left",font=Font)
    def game_over(self):
        self.goto(0,0)
        self.write( "GAME OVER!!!",align="center",font=Font)
    def increase_score(self):
        self.level+=1
        self.clear()
        self.update()

