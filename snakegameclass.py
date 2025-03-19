from turtle import Screen, Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)] #CONSTANT
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)
    
    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, i):
        new_segment = Turtle(shape = "circle")
        new_segment.color("Green")
        new_segment.penup()
        new_segment.goto(i)
        self.segments.append(new_segment)
    
    def extend(self):
        # self.add_segment((self.segments[-1].xcor(), self.segments[-1].ycor()))
        # or
        self.add_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments) - 1 , 0 ,-1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x,new_y)
        
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
          

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
