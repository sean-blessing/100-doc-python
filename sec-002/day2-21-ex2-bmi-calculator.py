#PEMDAS: Parenthesis, Exponents, Mult, Div, Add, Sub
#BMI calc = (lbs / (height inches)squared)*703
height_str = input("enter height in inches: ")
weight_str = input("enter weight in lbs: ")

height = int(height_str)
weight = float(weight_str)

bmi = (weight / (height**2))*703
print("bmi is "+str(bmi))