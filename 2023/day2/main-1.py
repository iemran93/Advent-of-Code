# 12 red cubes, 13 green cubes, and 14 blue cubes
with open("data.txt", "r") as file:
    content = file.read().split("\n")
gameposs = 0
for game, line in enumerate(content):
    possible = True
    config = line.split(":")[1]
    config = config.replace(" ", "").replace(",", "")
    config = config.split(";")
    for set in config:
        cubes = {"r": 0, "g": 0, "b": 0}
        set = set.replace("red", "r").replace(
            "green", "g").replace("blue", "b")
        i = 0
        while i < len(set):
            if set[i].isdigit():
                if set[i+1].isdigit():
                    cubes[set[i+2]] += int(set[i])*10+int(set[i+1])
                    i += 3
                else:
                    cubes[set[i+1]] += int(set[i])
                    i += 2
        if cubes["r"] > 12 or cubes["g"] > 13 or cubes["b"] > 14:
            possible = False
            break
    if possible:
        gameposs += (game+1)


print(gameposs)
