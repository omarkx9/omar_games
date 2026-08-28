# from turtle import Screen,Turtle
# from Documents.GitHub.Snake_game.snake import Snake
# from Documents.GitHub.Snake_game.food import Food
# from Documents.GitHub.Snake_game.score_bord import Score_Board
import time
from turtle import Screen,Turtle
from snake import Snake
from food import Food
from score_bord import Score_Board
import time

window = Screen()
window.setup(800,800)
window.title("Snake Game")
window.getcanvas().winfo_toplevel().resizable(False, False)

y = Turtle()
y.hideturtle()
y.penup()
y.color("gold")

def exit():
    global game_on
    game_on =  False

def not_complete():
    global complete
    complete = False

complete = True

while complete:
    window.onkey(not_complete,"q")
    window.clear()
    window.listen()

    window.tracer(0)

    snake = Snake()
    snake.creat_snake()

    score = Score_Board()

    apple = Food()
    apple.appear()

    game_on = True
    while game_on:
        window.bgcolor("dark gray")
        score.display()
        y.goto(0,320)
        y.write(f"..Press (Q) To Exit..", align = "center", font= ("arial",13))
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
    if play_again and play_again.lower() in ["y","yes","نعم"]:
        time.sleep(1)
        continue
    else:
        writer = Turtle()
        window.clear()
        writer.hideturtle()
        writer.color("gold")
        window.bgcolor("salmon")
        writer.goto(0,0)
        writer.write("GoodBye",align= "center",font=("arial",30,"bold"))
        time.sleep(3)
        break
        
        