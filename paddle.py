from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.setposition(position)
        self.shape("square")
        self.setheading(90)
        self.penup()
        self.shapesize(1,5)
        self.color('white')

    def go_up(self):
        self.forward(20)
    def go_down(self):
        self.backward(20)
