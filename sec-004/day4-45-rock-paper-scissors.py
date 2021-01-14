import random
choice = int(input("What do you choose (0 - rock, 1 - paper, 2 - scissors)?"))
#rock(0) > scissors(2), scissors(2) > paper(1), paper(1) > rock(0)
pc_choice = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
print(f"You chose:\n{game_images[choice]}")

print(f"PC chose:\n{game_images[pc_choice]}")

# determine if you won
result = "";
if choice==0 and pc_choice==2:
    result = "win!"
elif choice==1 and pc_choice==0:
    result = "win!"
elif choice==2 and pc_choice==1:
    result = "win!"
elif choice == pc_choice:
    result = "draw"
else:
    result = "lose"

print(f"You {result}")
