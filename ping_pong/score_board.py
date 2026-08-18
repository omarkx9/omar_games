from turtle import Turtle

class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(x,y)
        self.write(self.score, align= "center", font= ("arial",40,"bold"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align= "center", font= ("arial",40,"bold"))