from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
wid =400
hei =400
screen.setup(width=wid, height=hei)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor()>int((screen.window_width()/2)-5) or snake.head.xcor()<-int((hei/2)-5) or snake.head.ycor()>int((wid/2)-5) or snake.head.ycor()<-int((wid/2)-5):
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
