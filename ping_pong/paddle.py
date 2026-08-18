from turtle import Turtle

class Paddel(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5,1)
        self.goto(x,y)

    def go_up(self):
        self.goto(self.xcor(),self.ycor()+50)

    def go_down(self):    
        self.goto(self.xcor(),self.ycor()-50)
        