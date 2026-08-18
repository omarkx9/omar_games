from turtle import Screen,Turtle
from paddle import Paddel
from ball import Ball
from score_board import Score
from main_menu import Menu
import time

menu = Menu()

window = Screen()
window.clear()
menu.write("\n\nFirst to (7) Wins", align="center", font= ("arial",40,"bold"))
window.setup(800,600)
window.title("::Ping, Pong::")
window.bgcolor("black")
window.listen()
window.tracer(0)

r_paddel = Paddel(350,0)
r_paddel.color("red")
l_paddel = Paddel(-350,0)
l_paddel.color("blue")

ball = Ball()

window.onkey(r_paddel.go_up,"Up")
window.onkey(r_paddel.go_down,"Down")

window.onkey(l_paddel.go_up,"w")
window.onkey(l_paddel.go_down,"s")

r_score = Score(80,200)
r_score.color("red")
l_score = Score(-80,200)
l_score.color("blue")

time_speed = 0.1

gameOn = True
while gameOn:
    if r_score.score < 7 and l_score.score < 7:
        window.update()
        time.sleep(time_speed)
        ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)

        if ball.ycor() >= 280 or ball.ycor() <= -280:
            ball.y_move *= -1

        if (ball.xcor() >= 330 and ball.distance(r_paddel) <= 50) or (ball.xcor() <= -330 and ball.distance(l_paddel) <= 50):
            ball.x_move *= -1
            time_speed -= 0.01

        if ball.xcor() > 330:
            ball.goto(0,0)
            ball.x_move *= -1
            l_score.update_score()
            time_speed = 0.1

        if ball.xcor() < -330:
            ball.goto(0,0)
            ball.x_move *= -1
            r_score.update_score()
            time_speed = 0.1
    else:
        gameOn = False

window.clear()
window.bgcolor("green")

y = Turtle()
y.hideturtle()
y.penup()
y.color("gray")

if r_score.score == 7: 
    y.write(f"{menu.first_name} \n  Win\nWow!Wow", align="center", font= ("arial",30,"bold"))
else:
    y.write(f"{menu.seconde_name} \n  Win\nWow!Wow", align="center", font= ("arial",30,"bold"))
time.sleep(4)
