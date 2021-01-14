# prompt user name
# prompt user for name of love interest
# count the # of times letters 'true' occur in each name - 1st digit
# count the # of times letters 'love' occur in each name - 2nd digit
# score <10 or >90 "you go together like coke and mentos"
# score 40 - 50 "you are alright together"
# output "Your score is x" + message above

name = input("What's your name? ")
name_lower = name.lower()
crush_name = input("Who's your crush?")
crush_lower = crush_name.lower()
combined = name_lower + crush_lower

score_1st_digit = combined.count("t")
score_1st_digit += combined.count("r")
score_1st_digit += combined.count("u")
score_1st_digit += combined.count("e")

score_2nd_digit = combined.count("l")
score_2nd_digit += combined.count("o")
score_2nd_digit += combined.count("v")
score_2nd_digit += combined.count("e")

msg = f"Your score is {score_1st_digit}{score_2nd_digit}"
sum = score_1st_digit*10+score_2nd_digit
print(f"debug: 1st {score_1st_digit}, 2nd {score_2nd_digit}, sum {sum}")
if sum < 10 or sum > 90:
    msg+=", you go together like coke and mentos."
elif sum > 40 or sum < 50:
    msg+=", you are alright together."
else:
    msg+="."

print(msg)