from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.color("gold")
        self.hideturtle()
        self.penup()
        self.goto(0,350)
        self.score = 0
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
        self.write(f"Score: {self.score}    High Score: {self.highscore}", align = "center", font= ("arial",15))

    def game_over(self):
        self.screen.clear()
        self.screen.bgcolor("dark red")
        self.goto(0,0)
        self.color("tomato")
        self.save_high_score()
        if self.score < self.highscore:
            self.write(f"-(ㆆ_ㆆ)- Game Over -(ㆆ_ㆆ)-\n\n    Your Score: {self.score}\n\n  Your High Score: {self.highscore}", align= "center", font=("arial",40,"bold"))

        elif self.score == self.highscore:
            self.write(f"-(ㆆ_ㆆ)- You Get The Same Score -(ㆆ_ㆆ)-\n\n    Your Score: {self.score}\n\n  Your High Score: {self.highscore}", align= "center", font=("arial",40,"bold"))

        else:
            self.write(f"-(❁´◡`❁)- Congratulations -(❁´◡`❁)- \n         !You Beat Your High Score!\n\n            Your New High Score: {self.highscore}", align= "center", font=("arial",20,"normal"))

    def exit(self):
        self.screen.clear()
        self.screen.bgcolor("gray")
        self.goto(0,0)
        self.color("dark gray")
        self.write("Press Any Where To Exit", align= "center", font=("arial",30,"bold"))