import art
# print logo
print(art.logo)

def add(nbr_1, nbr_2):
    return nbr_1 + nbr_2

def subtract(nbr_1, nbr_2):
    return nbr_1 - nbr_2

def multiply(nbr_1, nbr_2):
    return nbr_1 * nbr_2

def divide(nbr_1, nbr_2):
    return nbr_1 / nbr_2

def print_result(nbr_1, opr, nbr_2, result):
    print(f"{nbr_1} {opr} {nbr_2} = {result}")
    return result

#store the functions inside a dictionary... cool!
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
choice = "y"
#Challenge:  change while loop to allow as many calculations as needed
# prompt for input:  number_1, operation (+, -, *, /), number_2
nbr_1 = float(input("What's the first number? "))
while choice == "y":
    operation = input("Pick an operation (+, -, *, /): ")
    nbr_n = float(input("What's the next number? "))
    # perform the calculation and print the full statement and result (4 + 2 = 6)
    calc_function = operations[operation]
    #we can dynamically call the function rather than using an if stmt!
    result = calc_function(nbr_1,nbr_n)
    print_result(nbr_1, operation, nbr_n, result)
    nbr_1 = result
    # prompt to continue calculating or goodbye
    choice = input(f"Press 'y' to continue calculating with {result}, or 'n' to exit. ")
print("bye")