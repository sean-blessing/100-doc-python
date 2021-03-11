# weather_file = open("./weather_data.csv", "r")
# data = weather_file.readlines()
# print(data)


# using csv
# import csv
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1].isdigit():
#             temp = int(row[1])
#             temperatures.append(temp)
#     print(temperatures)

# using pandas
import pandas


#data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print (temp_list)
#
# sum = sum(temp_list)
#
# print(f"sum = {sum}")
# print(f"avg = {sum / len(temp_list)}")
# mean = data["temp"].mean()
# temp_max = data["temp"].max()
# temp_min = data["temp"].min()
#
# print(f" series mean: {mean}")
# print(f" series max: {temp_max}")
# print(f" series min: {temp_min}")
#
# print(f"data conditions: {data.condition}")

# getting rows of data
# print row Monday
# print(data[data.day == "Monday"])
#
# # get row of highest temp
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# #convert monday temp to farenheit
# # f = (c * 1.8) + 32
# print(f"Monday temp in f: {(int(monday.temp)*1.8) + 32}")

#create data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# create csv file of squirrel counts
squirrel_data = pandas.read_csv("2018_Squirrel_Data.csv")
print(type(squirrel_data))
color_list = squirrel_data["Primary Fur Color"].to_list()
#Gray, Cinnamon, Black
count_gray = color_list.count("Gray")
count_cin = color_list.count("Cinnamon")
count_black = color_list.count("Black")

print(f"g{count_gray}, c{count_cin}, b{count_black}")
squirrel_dict = {
    "color": ["Gray", "Cinnamon", "Black"],
    "count": [count_gray, count_cin, count_black]
}
print(squirrel_dict)
squirrel_count_data = pandas.DataFrame(squirrel_dict)
squirrel_count_data.to_csv("squirrel_count.csv")