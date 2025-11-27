import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)

cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_squirrels_count)


new_squirrel_data_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_squirrels_count, grey_squirrels_count, cinnamon_squirrels_count]
}

new_DataFrame = pandas.DataFrame(new_squirrel_data_dict)
new_DataFrame.to_csv("Squirrel_Count.csv")
print(new_DataFrame)