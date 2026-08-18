from turtle import Turtle
import time

class Menu(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("dark gray")
        self.screen.bgcolor("gray")
        self.first_name = self.screen.textinput("Player Name","What IS The first player name?".title()).capitalize()
        self.seconde_name = self.screen.textinput("Player Name","What is the seconde player name?".title()).capitalize()
        self.write(f"Welcome {self.first_name}\n     and {self.seconde_name}",align= "center",font=("arial",30))
        time.sleep(2)
        self.clear()
        self.write(f"{self.first_name} You are The (Red)\n{self.seconde_name} You are The (blue)",align= "center",font=("arial",30,"bold"))
        time.sleep(2)
        self.clear()
        self.write(f"Give me one seconde Please...",align= "center",font=("arial",30,"bold"))
        time.sleep(2)

        