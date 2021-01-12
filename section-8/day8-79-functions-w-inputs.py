# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet(name):
    print(f"Hello {name}")
    print("Happy Monday")
    print("Let's code!")

greet("Sean")

def greet_with_location(name, location):
    print(f"Hello {name}")
    print(f"How is it in {location}?")
greet_with_location("Sean","Cincy")
greet_with_location(location="Indy",name="Tommy")