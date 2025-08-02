from turtle import  Screen
from paddle import Paddle
from Ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.title("Pong Pong !!")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Score()
# r_score=Score()
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

is_on=True
while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.update_score()
    if ball.ycor()>300 or ball.ycor()<-300:
         ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<320:
        ball.bounce_x()
    if ball.xcor() > 380:
       ball.reset_to_position()
       score.increase_left_side()
    if ball.xcor() < -380:
        ball.reset_to_position()
        score.increase_right_side()
screen.exitonclick()