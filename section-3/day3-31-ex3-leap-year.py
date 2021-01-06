# leap year evenly divisible by 4
# except when year evenly divisible by 100
# unless when year also evenly divisible by 400
year = int(input("What year would you like to check? "))

result = "Not Leap!"

if year%4==0:
    result = "Leap!"
    if year%100==0:
        result = "Not Leap!"
        if year%400==0:
            result = "Leap!"

print(result)
