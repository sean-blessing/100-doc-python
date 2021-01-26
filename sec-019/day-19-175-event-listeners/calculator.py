def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# passing a function as input, a higher order function
def calculator(n1, n2, func):
    return func(n1, n2)


print(calculator(2, 3, add))
