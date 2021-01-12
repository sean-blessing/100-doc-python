student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
#91 - Outstanding
#81 - Exceeds Expectations
#71 - Acceptable
#<71 - Fail
#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    grade = "Fail"
    score = student_scores[student]
    if score >=91:
        student_grades[student] = "Outstanding"
    elif score >=81:
        student_grades[student] = "Exceeds Expectations"
    elif score >=71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)