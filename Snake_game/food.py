from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        self.food_colors = [
    "#FF3131",
    "#FF8C00",
    "#FFD700",
    "#00E5FF",
    "#A855F7",
    "#FF2D95"
    ]
        self.food_shapes = ["circle","circle","circle","square","triangle","circle","circle"]
        super().__init__()
        self.penup()
        self.shapesize(0.5,0.5)

    def update_food(self):
        self.food_shape = random.choice(self.food_shapes)
        self.food_color = random.choice(self.food_colors)
        return [self.food_shape,self.food_color]

    def appear(self):
        colorANDshape = self.update_food()
        self.shape(colorANDshape[0])
        self.color(colorANDshape[1])
        self.goto(random.randint(-570,570),random.randint(-470,470))

    def food_pos(self):
        return self.pos()