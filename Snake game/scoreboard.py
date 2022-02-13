from turtle import  Turtle

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.shape(None)
        self.penup()
        self.goto(0,270)
        self.score=0
        self.hideturtle()
        self.update()


    def update(self):
        self.write(f"Score:{self.score}", False, 'center', ('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, 'center', ('Arial', 15, 'normal'))


    def increase_count(self):
        self.score+=1
        self.clear()
        self.update()
