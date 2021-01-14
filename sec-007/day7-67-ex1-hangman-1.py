import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and 
# assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)
letter_count = len(chosen_word)
    
#TODO-2 - Ask the user to guess a letter and assign their 
# answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter of the word: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) 
# is one of the letters in the chosen_word.
for n in range (0, letter_count):
    if chosen_word[n] == guess:
        print("right")
    else:
        print("wrong")
    # idx = chosen_word.find(str(guess))
    # if idx != -1:
    #     print(f"you guessed correct..  index = {idx}")