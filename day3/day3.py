
dict_lower = {chr(i): i-96 for i in range(97, 123)}
dict_upper = {chr(i): i-38 for i in range(65, 91)}

with open("day3\input.txt", 'r') as file:
    data = file.read().replace("\n", ",")
rucksacks = data.split(",")[:-1]

sum = 0

for rucksack in rucksacks:
    hf = int(len(rucksack)/2)
    comp1 = rucksack[:hf]
    comp2 = rucksack[hf:]
    common = set(comp1) & set(comp2)
    char = list(common)[0]

    if char in dict_lower:
        sum += dict_lower[char]
    else:
        sum += dict_upper[char]
print(sum)
