
dict_lower = {chr(i): i-96 for i in range(97, 123)}
dict_upper = {chr(i): i-38 for i in range(65, 91)}

with open("day3\input.txt", 'r') as file:
    data = file.read().replace("\n", ",")
rucksacks = data.split(",")[:-1]

sum = 0
group_id = 0

for group in range(3, len(rucksacks)+1, 3):
    part = rucksacks[group-3:group]
    common = set(part[0]) & set(part[1]) & set(part[2])
    char = list(common)[0]

    if char in dict_lower:
        sum += dict_lower[char]
    else:
        sum += dict_upper[char]

print(sum)
