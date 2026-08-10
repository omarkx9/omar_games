from turtle import Turtle,Screen
import random
import time

window = Screen()
window.title("Omar Turtle Race 🐢🏁")
window.setup(800,400)


while True:
    window.clear()
    window.bgcolor("gray")
    y = Turtle("turtle")
    y.hideturtle()
    y.color("white")
    y.write("😑GOOOOO!!😑",align="center",font=("arial",50))

    user_choice = window.textinput("!Guess the Winner! 🏆","Type a color: Red, Blue or Green? 🎨")
    words = ["أحمر","احمر","أزرق","ازرق","أخضر","اخضر","red","blue","green"]
    if user_choice in words:
        WY = [-70,0,70]
        colors = ["red","blue","green"]
        turtles = []

        for x in range(3):
            turtle = Turtle("turtle")
            turtles.append(turtle)
            turtles[x].color(colors[x])
            turtles[x].penup()
            turtles[x].goto(-280,WY[x])

        turtles[0].color("black")
        turtles[0].pensize(8)
        turtles[0].goto(280,0)
        turtles[0].pendown()
        turtles[0].left(90)
        turtles[0].forward(200)
        turtles[0].left(180)
        turtles[0].forward(800)
        turtles[0].penup()
        turtles[0].color("red")
        turtles[0].goto(-280,-70)
        turtles[0].left(90)

        def turn_to_english(word):
            if word == "احمر" or word == "أحمر":
                return "red"
            elif word == "ازرق" or word == "أزرق":
                return "blue"
            elif word == "اخضر" or word == "أخضر":
                return "green"
            else:
                return word

        def rice():
            game_on = True
            while game_on:
                for x in turtles:
                    if x.xcor() >= 280:
                        game_on = False
                        display_result(turn_to_english(user_choice) == x.color()[0],turn_to_english(x.color()[0]))
                        break
                    else:
                        x.forward(random.randint(1,5))

        def display_result(user,wineer):
            window.clear()
            window.bgcolor("red")
            result = Turtle()
            result.hideturtle()
            result.penup()
            result.color("white")
            if user:
                window.bgcolor("green")
                result.write(f"You Chose {turn_to_english(user_choice)}\nYou Win😎",align="center",font=("arial",20))
            else:
                result.write(f"You Chose {turn_to_english(user_choice)}\nYou Lose😑\nThe Wineer Was {wineer}",align="center",font=("arial",20))
            time.sleep(3)


        rice()

        sam = Turtle()
        window.clear()
        window.bgcolor("gray")
        sam.hideturtle()
        sam.color("dark gray")
        sam.goto(0,0)
        sam.write("Press any key to Exit... 👋",align="center",font = ("arial",30))
        break

    else:
        window.clear()
        window.bgcolor("gray")
        y = Turtle("turtle")
        y.hideturtle()
        y.color("white")
        y.write("Invalid Choice... 😑❌",align="center",font=("arial",50))
        time.sleep(2)
        continue
window.exitonclick()