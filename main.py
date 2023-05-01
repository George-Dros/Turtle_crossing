import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

TIME = 0.1
scoreboard = Scoreboard()
player = Player()
cars = []


screen.listen()
screen.onkey(player.go_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(TIME)
    screen.update()

    New_car = CarManager()
    cars.append(New_car)

    for car in cars:
        car.move()
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.game_over()

    if player.crossed():
        scoreboard.increase_score()
        cars = []
        TIME *= 0.9


screen.exitonclick()
