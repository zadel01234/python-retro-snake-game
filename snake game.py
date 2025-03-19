from turtle import Screen, Turtle
from snakegameclass import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Zadel's Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
board = Scoreboard()


screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down )
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.increase_score()

    # detect collision with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        board.reset()
        snake.reset()

    # detect collision with tail

    for i in snake.segments[1:]:
        if snake.head.distance(i) < 10:
            board.reset()
            snake.reset()
            
            




    # for i in snake.segments:
    #     if i == snake.head:
    #         pass
    #     elif snake.head.distance(i) < 10:
    #         board.game_over()
    #         game_is_on = False

    #     or 



screen.mainloop()