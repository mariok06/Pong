from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.color('MediumBlue')
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.setpos(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
