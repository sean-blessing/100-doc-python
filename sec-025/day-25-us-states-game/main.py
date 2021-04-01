import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_guesses = []
guess = ""
states_data = pandas.read_csv("50_states.csv")
# convert state to lower case
states_data["state"] = states_data["state"].str.lower()
states_list = states_data.state.to_list()


def print_state(state_str):
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    row = states_data[states_data.state == state_str]
    x_pos = int(row.x)
    y_pos = int(row.y)
    text_turtle.setpos(x_pos, y_pos)
    text_turtle.write(guess)


while len(correct_guesses) < 50:
    nbr = len(correct_guesses)
    header_str = "" + str(nbr) + "/50 States Correct"
    guess = screen.textinput(title=header_str, prompt="What's another state?")
    # convert guess to lowercase
    guess_lower = guess.lower()
    # check if guess is one of the 50 states in the csv file

    if guess_lower in states_list and guess_lower not in correct_guesses:
        # store guess in correct_guesses
        correct_guesses.append(guess_lower)
        # add state to map
        print_state(guess_lower)
    elif guess_lower == "exit":
        # save states_not_guessed.csv
        states_not_guessed = []
        # day 26 list comprehension challenge - cut down this code with list comp
        states_not_guessed = [state for state in states_list if state not in correct_guesses]
        not_guessed_data = pandas.DataFrame(states_not_guessed)
        not_guessed_data.to_csv("states_not_guessed.csv")
        # for state in states_list:
        #     if state not in correct_guesses:
        #         states_not_guessed.append(state)
        # not_guessed_data = pandas.DataFrame(states_not_guessed)
        # not_guessed_data.to_csv("states_not_guessed.csv")
        break



# code to determine x & y coords inside an image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# # keeps screen open
