from turtle import Turtle
import random

class Snake:

    def __init__(self):
        self.turtels = []
        self.positins = [(-20,0),(0,0),(20,0)]  
        self.colors = ["green","white"]
        
    def creat_snake(self):
        for x in range(len(self.positins)):
            self.turtels.append(Turtle("square"))
            self.turtels[x].color(random.choice(self.colors))
            self.turtels[x].penup()
            self.turtels[x].goto(self.positins[x])
        self.head = self.turtels[-1]
        self.head.color("orange")

    def extend(self):
        new_segment = Turtle("square")
        new_segment.color(random.choice(self.colors))
        new_segment.penup()
        new_segment.goto(self.turtels[0].pos())
        self.turtels.insert(0,new_segment)

    def move(self,number_of_move=20):
        for x in range(len(self.turtels)-1):
            self.turtels[x].goto(self.turtels[x+1].pos())
        self.head.forward(number_of_move)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

    def head_pos(self):
        return self.head.pos()
