student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

# using for loop
# for (key, value) in student_dict.items():
#     print(value)

# using pandas iterrows
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# loop thru data frame
# for (key, value) in student_data_frame.items():
#     print(value)
for (index, row) in student_data_frame.iterrows():
    #each row is a panda series
    print(row.score)