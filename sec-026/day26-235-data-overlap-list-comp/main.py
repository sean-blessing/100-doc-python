#read list of numbers in file1 and file2 and produce a new list of the numbers in common

with open("file1.txt", "r") as text_file_1:
    lines_1 = [int(nbr) for nbr in text_file_1.readlines()]

print(f"lines1 = {lines_1}")

with open("file2.txt", "r") as text_file_2:
    lines_2 = [int(nbr) for nbr in text_file_2.readlines()]

print(f"lines2 = {lines_2}")

common_nbrs = [nbr for nbr in lines_1 if nbr in lines_2]
print(f"commong_nbrs = {common_nbrs}")
