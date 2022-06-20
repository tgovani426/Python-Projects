from turtle import Turtle, Screen
import time
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600, starty=20)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
Scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #  detect collition with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle:
    if ball.distance(r_paddle) < 50 and  ball.xcor() > 330:
        ball.bounce_x()


    if ball.distance(l_paddle) < 50 and  ball.xcor() < -330:
        ball.bounce_x()
 
    # Detect the R paddle miss the ball
    if ball.xcor() >380:
        Scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        Scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
