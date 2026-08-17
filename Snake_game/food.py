from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        self.food_color = ["red","dark red","dark blue"]
        super().__init__()
        self.shape("circle")
        self.color(random.choice(self.food_color))
        self.penup()
        self.shapesize(0.5,0.5)

    def appear(self):
        self.goto(random.randint(-380,380),random.randint(-380,380))
    def food_pos(self):
        return self.pos()