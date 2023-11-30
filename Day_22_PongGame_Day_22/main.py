# Breaking down the problem for pong game.
# i. Create the screen
# ii. Create and move a paddle
# iii. Creater another paddle
# iv. Create the ball and make it move
# v. Detect collision with wall and bounce.
# vi. Detect collision with paddle.
# vii. Detec when paddle misses.
# viii. keep Score
from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import pygame
import time
game_is_on = True

screen = Screen()
# Creating window screen
screen.tracer(0)  # Turn off animation
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# Creating paddles
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
# Ball Object.
ball = Ball()
# Score board
scoreboard = Scoreboard()
# setting sound library


def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# setting timer for game
game_duration = 120  # 2 minute
start_time = time.time()

# Rest of the code...

# Create a Turtle object for displaying time
timer_turtle = Turtle()
timer_turtle.color("white")
timer_turtle.penup()
timer_turtle.goto(0, 260)
timer_turtle.hideturtle()
# _______________________________________


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


while game_is_on:
    # slowing the ball movement  using time.
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Rest of the code...
    
    # Calculate remaining time
     # Calculate elapsed time
    elapsed_time = time.time() - start_time
    remaining_time = game_duration - elapsed_time
    minutes = int(remaining_time // 60)
    seconds = int(remaining_time % 60)
    time_text = f"Time: {minutes:02d}:{seconds:02d}"
    
    # Clear previous time display
    timer_turtle.clear()
    
    # Display remaining time
    timer_turtle.write(time_text, align="center", font=("Arial", 16, "normal"))

    # Check if game duration has exceeded 1 minute
    elapsed_time = time.time() - start_time
    if elapsed_time >= game_duration:
        if scoreboard.r_score > scoreboard.l_score:
            timer_turtle.goto(0,0)
            timer_turtle.write("Game Over\nRight  win🥇\n\n\nGame Dev: NAZEEM KHAN", align="center",
                   font=("Courier", 30, "normal"))
        elif scoreboard.l_score>scoreboard.r_score:
            timer_turtle.goto(0,0)
            timer_turtle.write("Game Over\nLeft  win 🥇\n\n\nGame Dev: NAZEEM KHAN", align="center",
                   font=("Courier", 30, "normal"))
        else:
            timer_turtle.goto(0,0)
            timer_turtle.write("Draw 😊\n\n\nGame Dev: NAZEEM KHAN", align="center",
                   font=("Courier", 30, "normal"))
        game_is_on = False
        

    # Detect collision of ball with upper wall and lower wall
    # and bounce it
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        # play_sound(
                # "F:\\U-DEMY-COURSES\\My_programms\\PongGame_Day_22\\sounds\\wall_hit.wav")

    if ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 340:
        if ball.ycor() < r_paddle.paddle.ycor() + 50 and ball.ycor() > r_paddle.paddle.ycor() - 50:
            ball.bounce_x()
            # play_sound(
            #     "F:\\U-DEMY-COURSES\\My_programms\\PongGame_Day_22\\sounds\\ball_hit.wav")
            # Adjust ball direction based on paddle hit position
            ball.setheading(180 - ball.heading())
        # Detect collision with left paddle
    elif ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -340:
        if ball.ycor() < l_paddle.paddle.ycor() + 50 and ball.ycor() > l_paddle.paddle.ycor() - 50:
            ball.bounce_x()
            # play_sound(
            #     "F:\\U-DEMY-COURSES\\My_programms\\PongGame_Day_22\\sounds\\ball_hit.wav")
            ball.setheading(180 - ball.heading())

    # Detect if the ball misses the r_paddles
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        # play_sound(
        #         "F:\\U-DEMY-COURSES\\My_programms\\PongGame_Day_22\\sounds\\miss.wav")

    # l_paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        # play_sound(
        #         "F:\\U-DEMY-COURSES\\My_programms\\PongGame_Day_22\\sounds\\miss.wav")


screen.exitonclick()
