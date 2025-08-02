import turtle
from turtle import Turtle,Screen
import random

screen=Screen()

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt= "which turtle will win the race ? Enter a color :")
colors=["red","orange","yellow","green","blue","purple"]
y=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
 new_turtle=Turtle(shape="turtle")
 new_turtle.penup()
 new_turtle.goto(x=-230, y=y[turtle_index])
 new_turtle.color(colors[turtle_index])
 all_turtles.append(new_turtle)
is_race_on=False
if user_bet:
    is_race_on=True
while is_race_on:
 for turtle in all_turtles:
  if turtle.xcor()>230:
        is_race_on=False
        winning=turtle.pencolor()
        if winning==user_bet:
            print("you've won!")
        else:
            print(f"you lose , the winner is {winning}")


  moves=random.randint(0,10)
  turtle.forward(moves)

screen.exitonclick()








