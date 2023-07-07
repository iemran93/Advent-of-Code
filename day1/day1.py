import pandas as pd

with open("day1\calories.txt", "r") as file:
    data = file.read().replace('\n', ',').replace(',,', '\n')
data_lst = data.split("\n")
data_lst_int = [sum(map(int, i.split(','))) for i in data_lst]

# maximum calories
# print(max(data_lst_int))

# sum of the top 3
# print(sum(sorted(data_lst_int, reverse=True)[:3]))
