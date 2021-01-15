############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import art

print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = "y"

while play_again=="y":
    choice = "y"
    game_over = False

    player_cards = []
    cpu_cards = []

    def draw():
        return random.choice(cards)

    def display_summary():
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print(f"Your cards: {player_cards}, current score: {score_hand(player_cards)}")
        print(f"Computer's first card: {cpu_cards[0]}")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")

    def display_final_summary():
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
        print(f"Your final hand: {player_cards}, final score: {score_hand(player_cards)}")
        print(f"Computer's final hand: {cpu_cards}, final score: {score_hand(cpu_cards)}")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")

    def score_hand(hand):
        #a hand will be an array of ints
        #sum hand
        #if sum > 21, loop thru hand & change any 11 to 1 then re-sum
        total = sum(hand)
        if total > 21:
            if 11 in hand:
                idx_11 = hand.index(11)
                hand[idx_11] = 1
        total = sum(hand)
        return total

    def is_game_over():
        # evaluate scores to see if game is over
        player_score = score_hand(player_cards)
        cpu_score = score_hand(cpu_cards)
        line_sep = "*===========================*"
        if player_score==cpu_score:
            # draw
            print(line_sep)
            print("draw")
            print(line_sep)
            return True
        elif cpu_score > 21:
            # cpu bust
            print(line_sep)
            print("Computer bust!!  You win!!!  :)")
            print(line_sep)
            return True
        elif player_score > 21:
            # player bust
            print(line_sep)
            print("BUST!  You lose.  :(")
            print(line_sep)
            return True
        elif cpu_score > player_score:
            # cpu wins
            print(line_sep)
            if cpu_score==21:
                print("Blackjack!  ")
            print(f"Computer wins:  {cpu_score} - {player_score}")
            print(line_sep)
            return True
        elif player_score > cpu_score:
            # player wins
            print(line_sep)
            if player_score==21:
                print("Blackjack!!!")
            print(f"You win!!!!!!!!  :) Your Score: {player_score} - CPU Score: {cpu_score}")
            print(line_sep)
            return True
        else:
            # no winner yet... continue
            return False

    #draw 2 cards for each player to start
    for _ in range (2):
        player_cards.append(draw())
        cpu_cards.append(draw())

    while choice =="y" and not game_over:
        display_summary()
        #player chooses 1st...  hit or stand?
        choice = input("Type 'y' to get another card (hit), 'n' to stand: ")
        if choice=="y":
            #hit
            player_cards.append(draw())
            player_score = score_hand(player_cards)
            if (player_score < 21):
                continue
        else:
            #stand
            #cpu draws until stand or bust
            bust = False
            cpu_score = 0
            while not bust:
                cpu_score = score_hand(cpu_cards)
                player_score = score_hand(player_cards)
                #print(f"* debug * cpu_score={cpu_score}, player_score={player_score}")
                if cpu_score > 21:
                    bust = True
                elif cpu_score < 17:
                    cpu_cards.append(draw())
                else:
                    break
        # evaluate game over?
        game_over = is_game_over()
        if game_over:
            display_final_summary()
    
    play_again = input("\nPlay again (y/n)? ")
    print("")
print("Bye")