from turtle import Turtle,Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.setpos(0,0)
        self.shape("circle")
        self.is_ball_moving =True
        self.x_move=2
        self.y_move=2
        

    def move_ball(self):
       if self.is_ball_moving:
            self.penup()
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x,new_y)

    def bounce(self):
        self.y_move*=-1
    
    def bounce_x(self):
        self.x_move*=-1

    def reset_pos(self):
        self.goto(0,0)
            
            
