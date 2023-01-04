
import pandas
from turtle import Turtle,Screen

screen =Screen()
turtle=Turtle()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
print(all_states)

guessed_states = []
missing_states = []

while len(guessed_states) <50 :
    user_input = screen.textinput(f"{len(guessed_states)}/50", "your guess").title()

    if user_input == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_dataframe = pandas.DataFrame(missing_states)
        missing_dataframe.to_csv("states to learn.csv")

    if user_input in all_states:
        guessed_states.append(user_input)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_input]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(user_input)


screen.exitonclick()