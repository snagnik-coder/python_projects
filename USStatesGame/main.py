import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
game_on = True
guessed = []

while len(guessed) < 50:
    state = screen.textinput(title=f"{len(guessed)}/50 States Guessed", prompt = "What's another state's name?").title()
    if state == "Exit":
        missing_states = []
        for name in state_list:
            if name not in guessed:
                missing_states.append(name)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if state in state_list:
        guessed.append(state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state)
          
