
# with open(r'weather_data.csv', 'r') as file:
#   data = file.readlines()
#   print(data)

# mport csv
#
# with open(r'weather_data.csv', 'r') as file:
#    csv_reader = csv.reader(file)
#    temperatures = []
#    for y in csv_reader:
#        if y[1] != "temp":
#            temperatures.append(int(y[1]))
#
#        print(y)
#    print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
data_dicts = data.to_dict()
data_heal = data["temp"].to_list()

print(data["temp"].max())

### Get data in rows
print(data[data.temp == "Monday"])

print(data[data.temp == data["temp"].max()])
# 6  Sunday    24     Sunny

monday = data[data.day =="Monday"]
print(monday)
monday_temp = (monday.temp[0] * 9/5) + 32
print(monday_temp)



#### Create a dataframe from scratch

data_dicts = {
    "students": ["Alice", "Bob", "Charlie"],
    "scores": [75, 56,65]
}

dejta =pandas.DataFrame(data_dicts)
print(dejta)
dejta.to_csv("new_cvs.csv")

#print(data_heal)
#together = 0
#for i in range(len(data_heal)):
#    together += data_heal[i]
#average = together / len(data_heal)
#print(average)



