import turtle
import time
starting_position=[(0,0),(-20,0),(20,0)]
Move_Forward=20
up=90
down=270
left=180
right=0
class Snake: #class names should be in pascal case
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head= self.segments[0]
        self.scn= turtle.Screen()

    def create_snake(self):
        for i in starting_position:

            self.add_segments(i)

    def add_segments(self,position):
        segment = turtle.Turtle("square")
        segment.color("red")
        segment.penup()  # remove the line
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())



    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newx, newy)

        self.head.forward(Move_Forward)
        #self.segments[0].left(90)

    def up(self):
        if(self.head.heading() != down): #This finds out the angle of orientation of turtle with respect to the base line
            self.head.setheading(90)
            self.time_out()


    def down(self):
        if (self.head.heading() != up):
            self.head.setheading(270)
            self.time_out()



    def right(self):
        if (self.head.heading() != left):
            self.head.setheading(0)
            self.time_out()


    def left(self):
        if (self.head.heading() != right):
            self.head.setheading(180)
            self.time_out()


    def time_out(self):
        self.c=0
        for i in range(0,10):
            self.c+=1
            self.scn.onkey(None, "Up")
            self.scn.onkey(None, "Down")
            self.scn.onkey(None, "Right")
            self.scn.onkey(None, "Left")

        '''self.scn.onkey(up(), "Up")
        self.scn.onkey(down(), "Down")
        self.scn.onkey(right(), "Right")
        self.scn.onkey(left(), "Left")'''
