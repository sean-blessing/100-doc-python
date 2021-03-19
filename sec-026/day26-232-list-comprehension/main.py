numbers = [1,2,3]

# new list adding 1 to each n in numbers
new_list = []
# changing a list old fashioned way
# for n in numbers:
#     n += 1
#     new_list.append(n)

# changing a list w/ list comprehension
new_list = [n+1 for n in numbers]
print(numbers)
print(new_list)

name = "Sean"
letters_list = [letter for letter in name]
print(letters_list)

# range 1,5, create new list w/ each # doubled
nbrs = range(1,5)
new_nbrs = [n*2 for n in nbrs]

print(new_nbrs)

#conditional list comprehension
names = ["Sean", "Bailey", "Amy", "Breck"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# create new list of names greater than 4 chars in upper case
long_names_upper = [name.upper() for name in names if len(name) > 4]
print(long_names_upper)