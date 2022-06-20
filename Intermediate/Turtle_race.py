from turtle import Turtle,Screen
import random
screen=Screen()
screen.bgcolor("black")
screen.setup(width=500,height=400)
user_bet=(screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? red,orange, yellow , green , blue, purple  \n\n Enter your colour: ")).lower()
colors=["red","orange", "yellow" , "green" , "blue", "purple"]
y_position=[-150,-100,-50,0,50,100]
is_race_on=False
all_turtle=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtle.append(new_turtle)



if user_bet:
    is_race_on=True


while is_race_on:
    for tim in all_turtle:
        if tim.xcor() > 230:
            is_race_on=False
            winning_colour= tim.pencolor()
            if winning_colour == user_bet:
                print(f"You've won!! The {winning_colour} color turtle is winner!!")
            else:
                print(f"You've lost!! The {winning_colour} color turtle is winner!!")
            
        rand_distance=random.randint(0, 10)
        tim.forward(rand_distance)
    

screen.exitonclick()
