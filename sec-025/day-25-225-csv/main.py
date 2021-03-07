# weather_file = open("./weather_data.csv", "r")
# data = weather_file.readlines()
# print(data)

import csv
with open("weather_data.csv") as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for row in data:
        print(row)
        if (row[1].isdigit()):
            temp = int(row[1])
            temperatures.append(temp)
    print(temperatures)