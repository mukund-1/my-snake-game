from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen =Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#35635b")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on  = True
while game_is_on:
    screen.update()
    time.sleep(.5)
    snake.move()


    #detect collision with the food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall.
    if snake.head.xcor() >298 or snake.head.xcor()< -298 or snake.head.ycor() >298 or snake.head.ycor()< -298:
       scoreboard.reset()
       snake.reset() 


    #detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            
    #if head collides with any segment in the tail:
      #trigger game_over

screen.exitonclick()
    

