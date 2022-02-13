import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

sc= turtle.Screen()
sc.setup(width=600, height=600)
sc.bgcolor("white")
sc.title("Snake Game")
sc.tracer(0)

snake = Snake()
food = Food()
scoreboard=Scoreboard()
listen=True

def activate():
    sc.onkey(snake.up, "Up")
    sc.onkey(snake.down, "Down")
    sc.onkey(snake.right, "Right")
    sc.onkey(snake.left, "Left")

sc.listen()


#deactivate(listen)
count=0
game_is_on=True

while( game_is_on):
    sc.update()
    time.sleep(0.1)

    snake.move()
    activate()
    if snake.head.distance(food)<15 :
        food.refresh()
        #print(food.random_x)
        count+=1
        snake.extend()
        scoreboard.increase_count()

    if snake.head.xcor() > 280 or snake.head.xcor() <-300 or snake.head.ycor() > 300 or snake.head.ycor() <-280 :
        game_is_on=False
        scoreboard.game_over()


        for seg in snake.segments:
            if seg != snake.head:

                if snake.head.distance(seg) <0:
                    game_is_on=False
                    scoreboard.game_over()



sc.exitonclick()








