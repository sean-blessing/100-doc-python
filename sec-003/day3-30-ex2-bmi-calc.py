# < 18.5 underweight
# 18.5 <= x < 25 normal
# 25 <= x < 30 overweight
# 30 <= x < 35 obese
# 35 <= x clinically obese
#BMI calc = (lbs / (height inches)squared)*703
height_str = input("enter height in inches: ")
weight_str = input("enter weight in lbs: ")

height = int(height_str)
weight = float(weight_str)

bmi = (weight / (height**2))*703
print("bmi is "+str(bmi))

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("obese")
else:
    print("clinically obese")