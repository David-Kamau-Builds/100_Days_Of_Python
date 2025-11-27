import pandas

weather_data = pandas.read_csv("weather_data.csv")
print(type(weather_data))
print(weather_data)

# row
temp_weather_data = weather_data["temp"]
print(type(temp_weather_data))

# dictionary
weather_data_dict = weather_data.to_dict()
print(weather_data_dict)

# data series to a python list
weather_data_list = weather_data["temp"].to_list
print(weather_data_list)

average_weather_temp = weather_data["temp"].mean()
print(average_weather_temp)

max_weather_temp = weather_data["temp"].max()
print(max_weather_temp)

# get data in columns
weather_data_condition_column = weather_data.condition
print(weather_data_condition_column)

# get data in rows
weather_data_monday_row = weather_data[weather_data.day == "Monday"]
print(weather_data_monday_row)

# get data in row where temp was max
weather_data_max_temp_row = weather_data[weather_data.temp == max_weather_temp]
print(weather_data_max_temp_row)

# covert Monday temp to Fahrenheit
monday = weather_data[weather_data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_Fahrenheit = monday_temp * 9/5 + 32

print(monday_temp_Fahrenheit)


# create a dataframe from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

scores_data = pandas.DataFrame(data_dict)
scores_data.to_csv("scores_data.csv")
print(scores_data)