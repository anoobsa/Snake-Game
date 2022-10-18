from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=265)
        self.hideturtle()
        self.write(arg=f"Score: {self.score}", align=ALIGN,  font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align=ALIGN,  font=FONT)
