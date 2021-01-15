#global variable
enemies = 1

def increase_enemies():
    #local variable    
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")