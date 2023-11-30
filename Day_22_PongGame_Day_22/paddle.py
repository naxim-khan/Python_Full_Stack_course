from turtle import *
screen = Screen()
screen.bgcolor("black")


class Paddle(Turtle):
    # Create and move a paddle
    def __init__(self, position):
        super().__init__()
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.pu()
        self.paddle.goto(position)
    # Moving paddle
    screen.listen()

    def go_up(self):
        self.new_y = self.paddle.ycor()+20
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.paddle.ycor()-20
        self.paddle.goto(self.paddle.xcor(), self.new_y)

    def paddle2_Position(self):
        self.paddle.goto(0, 370)
