# small pizza: $10
# medium:  $20
# large: $25
# pepperoni:  $2 (small) $3 (med, large)
# x-cheese:  $1 (any)

print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want (S,M,L)? ")
if size == "S":
    bill += 10
elif size == "M":
    bill +=20
else:
    bill +=25
add_pepperoni = input("Want pepperoni(Y/N)? ")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3
extra_cheese = input("Want extra cheese(Y/N)? ")
if extra_cheese=="Y":
    bill += 1

print(f"Your final bill is {bill}.")


