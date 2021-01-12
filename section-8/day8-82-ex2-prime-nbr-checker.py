#Write your code below this line 👇
factors = []
def prime_checker(number):
    for n in range (1, number+1):
        if number%n==0:
            factors.append(n)
            print(f"{n} added to factors")

    if len(factors)==2:
        print("prime #")
    else:
        print("Not prime #")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)