from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-100, 200)
        self.write(f"Level: {self.score}", move=False, align="center", font=FONT)

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):

        self.write(f"Level: {self.score}", move=False, align="center", font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)
