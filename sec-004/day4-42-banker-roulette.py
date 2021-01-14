import random

names = input("Names (comma separated)? ")
names_list = names.split(", ")

print(names_list)

#r = random.randint(0,len(names_list)-1)
#print(f"Lucky buyer: {names_list[r]}")

# use 'choice' instead
print(f"Lucky buyer: {random.choice(names_list)}")