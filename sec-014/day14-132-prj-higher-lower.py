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

a_data = get_data()
score = 0
while not game_over:
    a_followers = a_data["follower_count"]
    b_data = get_data()
    b_followers = b_data["follower_count"]

    print(f"Compare A: {get_data_display_string(a_data)}")
    print(art.vs)
    print(f"Compare B: {get_data_display_string(b_data)}")
    
    choice = input("\nWho has more followers (A/B)?")
    if choice == "A":
        if a_followers > b_followers:
            score += 1
            print(f"You're right!  Current score: {score}.")
        else:
            game_over = True
    elif choice == "B":
        if b_followers > a_followers:
            score += 1
            print(f"You're right!  Current score: {score}.")
            a_data = b_data
        else:
            game_over = True
    else:
        print("invalid selection")
print(f"Sorry, that's wrong.  Final score: {score}")