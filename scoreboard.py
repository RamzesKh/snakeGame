from turtle import Turtle

class ScoreBoards(Turtle):
    def __init__(self):
        super().__init__()
        with open("score.txt", "r") as file:
            self.highestScore = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score} : Highest Score {self.highestScore}",align="center", font=("Arial",24,"normal"))

    def updateTheScore(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score} : Highest Score {self.highestScore}",align="center", font=("Arial",24,"normal"))

    def reset(self):
        if self.score > self.highestScore:
            self.highestScore = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.highestScore))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} : Highest Score {self.highestScore}",align="center", font=("Arial",24,"normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
