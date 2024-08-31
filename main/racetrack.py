import random
import turtle
from turtle import Turtle,Screen
screen = Screen()
background = 'racetrack.png'
screen.bgpic(background)


is_race_on = False
colours = ["red","black","purple","blue"]
y_positions = [-340,-120,110,320]
all_turtles = []

screen.setup(width=600, height=800)
user_bet = screen.textinput(title= "Make your bet",prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)


for turtle_index in range(0,4):
    new_turtle = Turtle(shape="circle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-400, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

    is_race_on = True


while is_race_on:

    for turtles in all_turtles:
        if turtles.xcor() > 350:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} circle is the won! ")
            else:
                print(f"You've lost! The {winning_color} circle is the won! ")


        rand_distance = random.randint(0,10)
        turtles.forward(rand_distance)




screen.exitonclick()
