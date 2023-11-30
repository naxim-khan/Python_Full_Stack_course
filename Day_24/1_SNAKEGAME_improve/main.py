from turtle import *
from snake import Snake
from food import Food
from scoreboard import Score
import time


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game.")

screen.tracer(0) # now the tracer is off

game_is_on=True

snake=Snake()
food=Food()
score=Score()




screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.update_score()
    # Detect collisoin with food
    if snake.head.distance(food) < 10:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        # score.game_over()
        score.reset()
        snake.reset()

        # game_is_on=False
    # Detect collision with tail
    for segment in snake.segments[2:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            snake.reset()
            score.game_over()



    
    





screen.exitonclick()