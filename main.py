from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=500)
screen.title('Pong')
screen.tracer(0)

POSITIONS = [(-350, 0), (350, 0)]

l_paddle = Paddle(POSITIONS[0])
r_paddle = Paddle(POSITIONS[1])

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    ball.move()

    # If the r_paddle misses.
    if ball.xcor() > 400:
        ball.reposition()
        scoreboard.increase_l_score()

    # If the l_paddle misses.
    elif ball.xcor() < - 400:
        ball.reposition()
        scoreboard.increase_r_score()

    # Detects collision with top & bottom walls.
    if ball.ycor() > 238 or ball.ycor() < -238:
        ball.bounce_y()

    # Detects collision with the paddles.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
