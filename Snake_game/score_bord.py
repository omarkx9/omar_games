from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,350)
        self.score = 0

    def display(self):
        self.write(f"Score: {self.score}", align = "center", font= ("arial",15))

    def game_over(self):
        self.screen.clear()
        self.screen.bgcolor("dark red")
        self.goto(0,0)
        self.color("gray")
        self.write(f"-_- Game Over -_-\n    Your Score: {self.score}", align= "center", font=("arial",40,"bold"))

    def exit(self):
        self.screen.clear()
        self.screen.bgcolor("gray")
        self.goto(0,0)
        self.color("dark gray")
        self.write("Press Any Where To Exit", align= "center", font=("arial",30,"bold"))