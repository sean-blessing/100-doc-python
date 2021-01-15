import art
import random

print(art.logo)

print("Welcome to the guess the number game!")
choice = "y"
while choice=="y":
    print("\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty level: (e)asy or (h)ard: ")
    attempts_remaining = 10 if difficulty=="e" else 5

    #get a random # between 1 and 100
    nbr = random.randint(1,100)
    nbr_guessed = False

    while attempts_remaining > 0 and not nbr_guessed:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts_remaining-=1
        if (guess > nbr):
            print("Too high.")
        elif (guess < nbr):
            print("Too low.")
        else:
            print(f"You got it!  The answer was {nbr}.")
            nbr_guessed = True
    if not nbr_guessed:
        print("You've run out of guesses.  You lose.")
    choice = input("Go again?")


print("Bye")