from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 25
        self.hideturtle()
        self.penup()
        self.goto(-290,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"LEVEL:{self.level}",align="left",font=FONT)
    
    def inc_level(self):
        self.level +=1
        self.update_score()
    
    def game_over(self):
        self.color("Dark Red")
        self.goto(-80,0)
        self.write(f"GAME OVER", align="left", font=FONT)
