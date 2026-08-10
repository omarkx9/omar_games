from turtle import Turtle,Screen
import random
import time

while True:
    window = Screen()
    window.setup(1000,1000)
    window.title("Omar Trutle Race")
    window.bgcolor("gray")
    user_choice = window.textinput("!Guess the winner!","Type a color: Red, Blue or Green?")

    words = ['red','blue','green',"احمر","ازرق","اخضر"]

    sam = Turtle("turtle")
    tom = Turtle("turtle")
    omar = Turtle("turtle")

    if user_choice.lower() in words:

        

        sam.color("light green")
        sam.penup()
        sam.pensize(5)
        sam.goto(480,500)
        sam.pendown()
        sam.left(90)
        sam.forward(500)
        sam.left(180)
        sam.forward(2000)
        sam.left(90)


        sam.color("green")
        tom.color("blue")
        omar.color("red")

        sam.speed("slowest")
        tom.speed("slowest")
        omar.speed("slowest")

        sam.penup()
        tom.penup()
        omar.penup()

        sam.goto(-480,250)
        tom.goto(-480,0)
        omar.goto(-480,-250)

        def race(turtle1,turtle2,turtle3):  
            turtle1.speed(random.choice(("fastest","fast","slow","slowest")))
            turtle2.speed(random.choice(("fastest","fast","slow","slowest")))
            turtle3.speed(random.choice(("fastest","fast","slow","slowest")))
            while True:
                turtle1.forward(random.randint(1,8))
                
                turtle2.forward(random.randint(1,8))
                
                turtle3.forward(random.randint(1,8))
                if turtle3.xcor() >= 480:
                    omar.write("Omar Win!",align="center",font="normal")
                    return ("red","احمر","أحمر")
                elif turtle2.xcor() >= 480:
                    tom.write("Tom Win!", align="center",font="normal")
                    return ("blue","ازرق","أزرق")
                elif turtle1.xcor() >= 480:
                    sam.write("Sam Win!",align="center",font="normal")
                    return ("green","اخضر", "أخضر")

        result = race(sam,tom,omar)

        window.clear()

        if user_choice.lower() in result:
            window.bgcolor("green")
            x = Turtle("turtle")
            x.hideturtle()
            x.penup()
            x.color("white")
            x.write("You Win!",align="center",font=("arial",80,"bold"))
        else:
            window.bgcolor("red")
            x = Turtle("turtle")
            x.hideturtle()
            x.penup()
            x.color("white")
            x.write(f"You Lose!\n{result[0]} Win",align="center",font=("arial",80,"bold"))

        time.sleep(3)
        break

        
    else:
        window.clear()
        window.bgcolor("gray")
        y = Turtle("turtle")
        y.hideturtle()
        y.color("white")
        y.write("Invalid Choice...😑",align="center",font= ("arial",50))
        time.sleep(5)
        continue

window.clear()
window.bgcolor("gray")
sam.hideturtle()
sam.color("dark gray")
sam.goto(0,0)
sam.write("Press any key to Exit...",align="center",font = ("arial",50))

window.exitonclick()