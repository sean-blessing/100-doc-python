# get list of student heights, separated by spaces
# convert the list to ints
# calculate the average height

heights_list = input("Enter student heights: ").split()
for n in range(0, len(heights_list)):
    heights_list[n] = int(heights_list[n])

print(f"Heights:  {heights_list}")
count = 0;
sum = 0;
for height in heights_list:
    count+=1
    sum+=height
avg = sum / count
print(f"Heights Sum: {sum}, Count: {count}, Average: {avg}")