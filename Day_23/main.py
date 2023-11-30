import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Road (By:--> Nazeem Khan)")
screen.setup(width=600, height=600)
screen.tracer(0)

#Player 
player = Player()
scoreboard = Scoreboard()
#cars
car_manager=CarManager()
# Move player by keyboard key's
screen.listen()
screen.onkeypress(player.up,"Up")         # Up movement    👆🏻
# screen.onkeypress(turtle.down,"Down")   # Down Movement   👇🏻
# screen.onkeypress(turtle.right,"Right") # Right Movement  👉🏻
# screen.onkeypress(turtle.left,"Left")   # Left Movement   👈🏻



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if int(car.distance(player)) < 20:
           player.write("☠", font=("Courier", 50))
           game_is_on = False
           scoreboard.game_over()
    #Detect successful crossing
    if player.is_at_finish_line():
        player.go_t0_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()