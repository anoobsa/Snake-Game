from turtle import Turtle
AXIS = [(0, 0), (-20, 0), (-40, 0)]
FOR_DIST = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.head.color("blue")
        self.head.shape("triangle")

    def create_snake(self):
        for position in AXIS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_list.append(snake_segment)

    def extend_snake(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            x_pos = self.snake_list[seg_num - 1].xcor()
            y_pos = self.snake_list[seg_num - 1].ycor()
            self.snake_list[seg_num].goto(x_pos, y_pos)
        self.head.forward(FOR_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

