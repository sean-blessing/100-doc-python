print("Here's a treasure map. It's currently empty:")
row1 = ['0','0','0' ]
row2 = ['0','0','0' ]
row3 = ['0','0','0' ]

map = [row1, row2, row3]
print(f"{map[0]}\n{map[1]}\n{map[2]}")

pos_str = input("Where do you want to put the treasure (\"row, column\")? ")
row_col_list = pos_str.split()
row = int(row_col_list[0])
col = int(row_col_list[1])
map[row-1][col-1] = "X"
print("X marks the spot!")
print(f"{map[0]}\n{map[1]}\n{map[2]}")

