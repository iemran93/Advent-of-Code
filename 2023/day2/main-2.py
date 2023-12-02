# 12 red cubes, 13 green cubes, and 14 blue cubes
with open("data.txt", "r") as file:
    content = file.read().split("\n")
totalpower = 0
for game, line in enumerate(content):
    possible = True
    config = line.split(":")[1]
    config = config.replace(" ", "").replace(",", "")
    config = config.split(";")
    cubes = {"r": [], "g": [], "b": []}
    for set in config:
        set = set.replace("red", "r").replace(
            "green", "g").replace("blue", "b")
        i = 0
        while i < len(set):
            if set[i].isdigit():
                if set[i+1].isdigit():
                    cubes[set[i+2]].append(int(set[i])*10+int(set[i+1]))
                    i += 3
                else:
                    cubes[set[i+1]].append(int(set[i]))
                    i += 2
    cubes = {key: max(value) for key, value in cubes.items()}
    power = cubes["b"]*cubes["g"]*cubes["r"]
    totalpower += power
print(totalpower)
