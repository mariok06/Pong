from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 28, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.goto(0, 195)
        self.color('cornflower blue')
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f'{self.l_score}    {self.r_score}', align=ALIGNMENT, font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_score()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_score()
