print("Welcome to the tip calculator.")

total_bill_str = input("What was the total bill? $")
total = float(total_bill_str)

tip_pct_str = input("What tip % would you like to give (10/12/15)?")
tip = int(tip_pct_str)/100

split_str = input("How many people to split the bill? ")
split = int(split_str)

bill_per_person = round((total*(1+tip))/split,2)

print(f"Each person should pay: ${bill_per_person}")
