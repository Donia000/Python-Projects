
colors=["red","orange","yellow","green","blue","purple"]
start_move=5
move_increment=10
import random
from turtle import Turtle
class Car:

    def __init__(self):
        self.all_cars=[]
        self.speed=start_move
    def create(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
         new_car = Turtle(shape="square")
         new_car.shapesize(stretch_len=2,stretch_wid=1)
         new_car.speed()
         new_car.penup()
         new_car.color(random.choice(colors))
         random_y=random.randint(-250,250)
         new_car.goto(300,random_y)
         self.all_cars.append(new_car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def high_speed(self):
            self.speed += move_increment


