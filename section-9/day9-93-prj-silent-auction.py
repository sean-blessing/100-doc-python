import art
#couldn't get the 'clear' function to work :(
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
print("Welcome to the secret auction program.")

choice = "y"
max_bid = 0
winner = ""
bids = {}

while choice=="y":
    name = input("What's your name?")
    bid = float(input("What's your bid? $"))
    bids[name] = bid
    choice = input("Are there any other bidders? ")
    clear()

for key in bids:
    if bids[key] > max_bid:
        winner = key
        max_bid = bids[key]
clear()
print(f"The winner is {winner} with a winning bid of ${max_bid}")


