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
window.title("Snake Game")

window.setup(1536,1024)
window.bgpic("all_pictures/start_menu.png")
continues = window.textinput("continue","press enter to continue".title())

if not continues:
    time.sleep(5)
elif continues.lower() == "fast" or continues.lower() == "high score zero":
    time.sleep(0.1)
else:
    time.sleep(2)

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
speed = 0.1

window.onkey(not_complete,"q")
window.listen()

game_on = True


while complete:
    window.clear()
    window.tracer(0)
    snake = Snake()
    snake.creat_snake()

    score = Score_Board()
    if continues == "high score zero":
            score.highscore = 0
            continues = "END"
            with open("high_score.txt","w") as f:
                f.write("0")
            score.old_highscore = 0
    apple = Food()
    apple.appear()
    while game_on:
        window.setup(1200,1000)
        window.bgpic("all_pictures/Snake_game_back_ground.png")
        score.display()
        y.goto(0,430)
        y.write(f"..Press (Q) To Exit..", align = "center", font= ("arial",13))
        snake.move()
        window.onkey(snake.up,"Up")
        window.onkey(snake.down,"Down")
        window.onkey(snake.right,"Right")
        window.onkey(snake.left,"Left")
        window.onkey(exit,"q")
        window.update()
        time.sleep(speed)
        if snake.head.distance(apple.food_pos())<15:
            if apple.food_shape == "triangle":
                score.score += 3
                snake.extend()
                snake.extend()
                snake.extend()
                speed -= 0.007
            elif apple.food_shape == "circle":
                score.score += 1
                snake.extend()
            elif apple.food_shape == "square":
                score.score += 5
                snake.extend()
                snake.extend()
                snake.extend()
                snake.extend()
                snake.extend()

            apple.appear()
        if snake.head.xcor() > 580 or snake.head.ycor() > 480 or snake.head.xcor() < -580 or snake.head.ycor() < -480:
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
        speed = 0.1
        continue
    else: 
        writer = Turtle()
        window.clear()
        window.setup(1672,941)
        writer.hideturtle()
        writer.color("gold")
        window.bgpic("all_pictures/goodbye.png")
        writer.goto(0,0)
        time.sleep(3)
        break
        
        