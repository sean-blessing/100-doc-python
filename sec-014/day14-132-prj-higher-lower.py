import art
import game_data
import random

print(art.logo)

game_over = False
data_list = game_data.data

def get_data():
    return random.choice(data_list)

def get_data_display_string(data):
    str = data["name"] + ", a " + data["description"] + ", from " + data["country"] + "."
    return str

while not game_over:
    a_data = get_data()
    b_data = get_data()

    print(f"Compare A: {get_data_display_string(a_data)}")
    print(art.vs)
    print(f"Compare B: {get_data_display_string(b_data)}")
    game_over = True



