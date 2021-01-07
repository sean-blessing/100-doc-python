# print each # from 1 to 100
# Fizz - if # is divisible by 3
# Buzz - if # is divisible by 5
# FizzBuzz - if # is divisible by 3 and 5

for n in range(1,101):
    msg = ""
    if n%3==0:
        msg+="Fizz"
    if n%5==0:
        msg+="Buzz"
    if n%3!=0 and n%5!=0:
        msg+=str(n);
    print(msg)
