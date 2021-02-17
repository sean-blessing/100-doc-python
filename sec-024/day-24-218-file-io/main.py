# 1st iteration
#file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# similar to try-with-resources. Auto closes file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# auto opens read only, change to write mode so it is editable, then change to append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nAnother new line.")
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# create a new file
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")

