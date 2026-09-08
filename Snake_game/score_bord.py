from turtle import Turtle
import time

class Score_Board(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("gold")
        self.hideturtle()
        self.penup()
        self.goto(0,450)
        self.score = 0
        self.old_highscore = self.get_high_score()
        self.highscore = self.get_high_score()

    def get_high_score(self):
        with open("high_score.txt") as file:
            return int(file.read())

    def save_high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score

        with open("high_score.txt","w") as file:
            file.write(str(self.highscore))

    def display(self):
        self.clear()
        self.save_high_score()
        self.write(f"Score: {self.score}    High Score: {self.highscore}", align = "center", font= ("arial",20))

    def game_over(self):
        self.screen.clear()
        self.goto(0,0)
        self.color("#00E5FF")
        self.save_high_score()

        if self.score < self.old_highscore:
            self.screen.setup(1536,1024)
            self.screen.bgpic("all_pictures/game_over.png")
            self.write(f"    Your Score: {self.score}\n\n  Your High Score: {self.highscore}", align= "center", font=("arial",70,"bold"))

        elif self.score == self.old_highscore:
            self.screen.setup(1672,941)
            self.screen.bgpic("all_pictures/draw.png")
            self.write(f"    Your Score: {self.score}\n\n  Your High Score: {self.highscore}", align= "center", font=("arial",70,"bold"))

        else:
            self.screen.setup(1672,941)
            self.screen.bgpic("all_pictures/win.png")
            self.write(f"      !You Beat Your High Score!\n\n         Your New High Score: {self.highscore}", align= "center", font=("arial",50,"normal"))

    def exit(self):
        self.screen.clear()
        self.screen.bgcolor("gray")
        self.goto(0,0)
        self.color("dark gray")
        self.write("Press Any Where To Exit", align= "center", font=("arial",30,"bold"))