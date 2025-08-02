import time
from turtle import Screen
from player import Player
from car_manager import Car
from score_board import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
player=Player()
score=Score()
car=Car()
screen.listen()
screen.onkey(player.up,"Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car.create()
    car.move_car()


    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()


    if player.ycor()==280:
        player.finishing()
        score.increase_score()
        car.high_speed()




screen.exitonclick()