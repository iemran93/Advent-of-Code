with open("2023/day4/data.txt") as file:
    content = file.read().split("\n")

content = [line.split(":")[1] for line in content]

matching = []
totalPoints = 0
for line in content:
    line = line.split("|")
    winNums = line[0].split(" ")
    myNums = line[1].split(" ")
    cardsWining = []
    for num in myNums:
        if num in winNums and num != "":
            cardsWining.append(num)
    matching.append(len(cardsWining))
    if len(cardsWining) != 0:
        points = 2**(len(cardsWining)-1)
        totalPoints += points

totalScratch = [1 for line in content]
for i, cop in enumerate(matching):
    for _ in range(totalScratch[i]):
        indx = i + 1
        for _ in range(cop):
            totalScratch[indx] += 1
            indx += 1

print("pt1: ", totalPoints)
print("pt2: ", sum(totalScratch))
