import turtle
import pandas
from stateTurtle import StateTurtle
screen = turtle.Screen()
screen.title("US States Game")
image = 'day-25-start/day-25-challenge/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

stateFrame = pandas.read_csv("day-25-start\day-25-challenge/50_states.csv")
f = stateFrame[stateFrame['state'] == 'California']
all_states = stateFrame.state.tolist()
guessed_states = []

print(f)
print(type(f['state'].item()))


st = StateTurtle()
game_is_on = True
while(game_is_on):
    answer_state = screen.textinput(title="Guess the state", prompt= "Enter a State Name").title()
    if(answer_state == "exit"):
        game_is_on = False
    
    state_row = stateFrame[stateFrame['state'] == answer_state]
    print(type(state_row))
    if(not state_row.empty):
        currPosition = (state_row['x'].item(), state_row['y'].item())
        st.write_StateName(position= currPosition, name=state_row['state'].item())
        guessed_states.append(answer_state)
    if(st.count == 50):
        game_is_on = False

missing_state = [state for state in all_states if state not in guessed_states]

stateSeries = pandas.DataFrame(missing_state)
stateSeries.to_csv("States_to_Learn.csv")


screen.exitonclick()