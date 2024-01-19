from turtle import Turtle

class Snake:
    def __init__(self):
        turtle_size = -20
        self.turtles = []
        for i in range(3):
            newTurtle = Turtle("square")
            newTurtle.color("white")
            newTurtle.setx(turtle_size * i)
            newTurtle.penup()
            newTurtle.clear()
            self.turtles.append(newTurtle)
        self.head = self.turtles[0]
        self.turtles[0].setheading(0)


    def add_segment(self):
        newTurtle = Turtle("square")
        newTurtle.color("white")
        newTurtle.penup()

        if self.turtles[0].heading() == 0 or self.turtles[0].heading() == 180:
            position_x = self.turtles[-1].xcor() - 20
            position_y = self.turtles[-1].ycor()
            newTurtle.setposition(position_x, position_y)
        else:
            position_x = self.turtles[-1].xcor()
            position_y = self.turtles[-1].ycor() - 20
            newTurtle.setposition(position_x, position_y)

        self.turtles.append(newTurtle)

    def reset(self):
        if len(self.turtles) > 3:
            for turtle in self.turtles[3:]:
                turtle.hideturtle()
                self.turtles.remove(turtle)
            print(len(self.turtles))
        self.turtles[0].goto(0,0)
        self.turtles[0].goto(-20,0)
        self.turtles[0].goto(-40,0)






    def move(self):
        for seg_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.turtles[0].forward(20)
    def Up(self):
        if self.turtles[0].heading() != 90 and self.turtles[0].heading() != 270:
            if self.turtles[0].heading() == 0:
                self.turtles[0].left(90)
                self.move()
            else:
                self.turtles[0].right(90)
                self.move()

    def Right(self):
        if self.turtles[0].heading() != 0 and self.turtles[0].heading() != 180:
            if self.turtles[0].heading() == 270:
                self.turtles[0].left(90)
            else:
                self.turtles[0].right(90)
            self.move()

    def Left(self):
        if self.turtles[0].heading() != 0 and self.turtles[0].heading() != 180:
            if self.turtles[0].heading() == 270:
                self.turtles[0].right(90)
            else:
                self.turtles[0].left(90)
            self.move()


    def Down(self):
        if self.turtles[0].heading() != 90 and self.turtles[0].heading() != 270:
            if self.turtles[0].heading() == 0:
                self.turtles[0].right(90)
                self.move()
            else:
                self.turtles[0].left(90)
                self.move()