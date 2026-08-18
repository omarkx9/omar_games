from turtle import Turtle

class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("orange")
        self.score = 0
        self.goto(x,y)

    def update_score(self):
        self.score += 1

    def update_display(self):
        self.clear()
        self.write(self.score, align= "center", font= ("courier",40,"bold"))

    