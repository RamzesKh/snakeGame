import time
from turtle import Turtle, Screen
from snake import Snake
from Food import Food
from scoreboard import ScoreBoards
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoards()


screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")


while game_is_on:

    screen.update()
    snake.move()
    time.sleep(0.05)

    if snake.head.distance(food) <20:
        food.refresh()
        scoreboard.updateTheScore()
        snake.add_segment()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() <-290:
        game_is_on = False
        scoreboard.gameOver()
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            game_is_on = False
            scoreboard.gameOver()






screen.exitonclick()