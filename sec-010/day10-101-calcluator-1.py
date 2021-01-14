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

#store the functions inside a dictionary... cool!
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
choice = "y"
while choice == "y":
    # prompt for input:  number_1, operation (+, -, *, /), number_2
    nbr_1 = float(input("Enter number 1: "))
    operation = input("Pick an operation (+, -, *, /): ")
    nbr_2 = float(input("Enter number 2:"))
    # perform the calculation and print the full statement and result (4 + 2 = 6)
    calc_function = operations[operation]
    #we can dynamically call the function rather than using an if stmt!
    first_result = calc_function(nbr_1,nbr_2)
    print_result(nbr_1, operation, nbr_2, first_result)
    
    #second operation
    operation = input("Pick an operation (+, -, *, /): ")
    nbr_3 = float(input("Enter number 3:"))
    calc_function = operations[operation]
    second_result = calc_function(first_result, nbr_3)
    print_result(first_result, operation, nbr_3, second_result)
    # prompt to continue
    choice = input("Press 'y' to continue? (y/n) ")
print("bye")