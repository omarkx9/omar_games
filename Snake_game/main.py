from turtle import Screen,Turtle
from Documents.GitHub.Snake_game.snake import Snake
from Documents.GitHub.Snake_game.food import Food
from Documents.GitHub.Snake_game.score_bord import Score_Board
import time


window = Screen()
window.setup(800,800)
window.title("Snake Game")
window.getcanvas().winfo_toplevel().resizable(False, False)

complete = True

while complete:
    window.clear()
    window.listen()

    window.tracer(0)
    def exit():
        global game_on
        game_on =  False

    snake = Snake()
    snake.creat_snake()

    score = Score_Board()

    apple = Food()
    apple.appear()

    game_on = True
    while game_on:
        window.bgcolor("dark gray")
        score.clear()
        score.display()
        snake.move()
        window.onkey(snake.up,"Up")
        window.onkey(snake.down,"Down")
        window.onkey(snake.right,"Right")
        window.onkey(snake.left,"Left")
        window.onkey(exit,"q")
        window.update()
        time.sleep(0.1)
        if snake.head.distance(apple.food_pos())<15:
            apple.appear()
            snake.extend()
            score.score += 1
        if snake.head.xcor() > 370 or snake.head.ycor() > 370 or snake.head.xcor() < -370 or snake.head.ycor() < -370:
            score.game_over()
            time.sleep(2)
            game_on = False
        for x in snake.turtels[:-1]:
            if snake.head.distance(x) < 10:
                score.game_over()
                time.sleep(2)
                game_on = False

    play_again = window.textinput("Play Again","Do You Want To Play Again?")
    if play_again and play_again.lower() == "y":
        continue
    else:
        writer = Turtle()
        window.clear()
        writer.hideturtle()
        writer.color("white")
        window.bgcolor("dark gray")
        writer.goto(0,0)
        writer.write("GoodBye",align= "center",font=("arial",30,"bold"))
        time.sleep(3)
        break
        
        