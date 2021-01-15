#a has global scope
if 2 < 3:
    a = 10

print(a)

#functions have block scope
def do_something():
    b = 20
#err - b is not defined
#print(b)

c=40
d=90

def print_c():
    c = 50
    print(c)
    #explicityly modify global c
    d = 100
print_c()
print(c)
