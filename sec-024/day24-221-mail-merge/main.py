names = open("./Input/Names/invited_names.txt", "r")
names_list = names.readlines()

def build_letter(recipient):
    template_letter = open("./Input/Letters/starting_letter.txt", "r")
    template_letter_lines = template_letter.readlines()
    with open(f"./Output/ReadyToSend/{name}_file.txt", mode="w") as file:
        for line in template_letter_lines:
            line = line.replace("\n", "")
            # for all lines in letter template, replace [name] with name argument and write to new file
            line = line.replace("[name]",name)
            file.write(f"{line}\n")

for name in names_list:
    name = name.replace("\n", "")
    print(f"generating letter for {name}")
    build_letter(name)


