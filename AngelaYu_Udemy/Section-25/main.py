# with open("weather_data.csv") as file:
#    data = file.readlines()
#    print(file.readlines())

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

print(f"{data}"
      f"\n\n"
      f"{data['temp']}"
      f"\n\n"
      f"{data['day']}")
