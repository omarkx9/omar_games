from turtle import Screen,Turtle
from paddle import Paddel
from ball import Ball
from score_board import Score
from main_menu import Menu
import time

window = Screen()

while True:
    window.bgcolor("gray")
    number_to_win = window.textinput("Number To Win","Write The number of win".title())
    if number_to_win:
        if number_to_win.isdigit():
            number_to_win = int(number_to_win)
            x = True
            break
    else:
        x = False

if x:

    def formater(r,l):
        if r.score > l.score:
            r.color("red")
            l.color("orange")
        elif r.score < l.score:
            r.color("orange")
            l.color("blue")
        else:
            r.color("orange")
            l.color("orange")
        r.update_display()
        l.update_display()


    menu = Menu()

    window.clear()

    

    menu.write(f"\n\nFirst to ({number_to_win}) Wins", align="center", font= ("arial",40,"bold"))
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
    l_score = Score(-80,200)

    time_speed = 0.08

    gameOn = True
    while gameOn:
        formater(r_score,l_score)
        if r_score.score < number_to_win and l_score.score < number_to_win:
            window.update()
            time.sleep(time_speed)
            ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)

            if ball.ycor() >= 280 or ball.ycor() <= -280:
                ball.y_move *= -1

            if (ball.xcor() >= 330 and ball.distance(r_paddel) <= 50) or (ball.xcor() <= -330 and ball.distance(l_paddel) <= 50):
                ball.x_move *= -1
                time_speed *= 0.9

            if ball.xcor() > 330:
                ball.goto(0,0)
                ball.x_move *= -1
                l_score.update_score()
                time_speed = 0.08

            if ball.xcor() < -330:
                ball.goto(0,0)
                ball.x_move *= -1
                r_score.update_score()
                time_speed = 0.08
        else:
            gameOn = False

    window.clear()
    window.bgcolor("green")

    y = Turtle()
    y.hideturtle()
    y.penup()
    y.color("gray")

    if r_score.score == number_to_win: 
        y.write(f"({menu.first_name}) \n  Win\nWow!Wow", align="center", font= ("arial",30,"bold"))
    else:
        y.write(f"{menu.seconde_name} \n  Win\nWow!Wow", align="center", font= ("arial",30,"bold"))
else:
    pass
window.mainloop()