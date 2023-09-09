from turtle import Turtle,Screen
from scoreboard import Scoreboard
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
from paddle import Paddle
from ball import Ball
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

# paddle = Turtle()
# paddle.speed("fast")
# paddle.setposition(350,0)
# paddle.shape("square")
# paddle.setheading(90)
# paddle.penup()
# paddle.shapesize(1,5)
# paddle.color('white')


right_ball = Ball()

screen.listen()
screen.onkey(key="Up",fun=r_paddle.go_up)
screen.onkey(key="Down",fun=r_paddle.go_down)
screen.onkey(key="w",fun=l_paddle.go_up)
screen.onkey(key="s",fun=l_paddle.go_down)

game_is_on = True
while game_is_on:
    screen.update()
    right_ball.move_ball()
    if right_ball.ycor()>=290:
        right_ball.bounce() 
    elif right_ball.ycor()<=-290:
        right_ball.bounce()

    if right_ball.distance(r_paddle)<50 and right_ball.xcor()>350:
        right_ball.bounce()
        right_ball.bounce_x()

    if right_ball.distance(l_paddle)<50 and right_ball.xcor()<-350:
        right_ball.bounce()
        right_ball.bounce_x()

    if right_ball.xcor()>390:
        right_ball.reset_pos()
        scoreboard.l_point()

    if right_ball.xcor()<-390:
        right_ball.reset_pos()
        scoreboard.r_point()
screen.exitonclick()
