import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


class StateWriter(turtle.Turtle):
    """A class to write state names on the map."""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state_name, x, y):
        """Moves the turtle to the given coordinates and writes the state name."""
        self.goto(x, y)
        self.write(state_name)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
state_writer = StateWriter()


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # Use a list comprehension for a more concise way to get missing states
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the answer is a valid state and hasn't been guessed yet
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_writer.write_state(answer_state, state_data.x.item(), state_data.y.item())