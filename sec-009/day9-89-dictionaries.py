# define a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and overa again."

}
#access an item in dictionary
#print(programming_dictionary["Loop"])

#add item to dictionary
programming_dictionary["If"] = "A keyword that allows execution of some code only if the condition is true."

#print whole dictionary
#print(programming_dictionary)

#create empty dictionary
new_dictionary = {}

#loop through keys of dictionary
for key in programming_dictionary:
    print(key+", "+programming_dictionary[key])
