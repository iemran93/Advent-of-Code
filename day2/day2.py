# (1 for Rock, 2 for Paper, and 3 for Scissors)
# (0 if you lost, 3 if the round was a draw, and 6 if you won)

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

sum = 0
lost, draw, won = 0, 3, 6
rock, paper, scissors = 1, 2, 3

with open("day2\input.txt", 'r') as file:
    data = file.read().split("\n")[:-1]
for round in data:
    x = round[0]
    y = round[2]
    # part 1
    '''match x:
        case "A":
            if y == "X":
                score = rock + draw
            elif y == "Y":
                score = paper + won
            else:
                score = scissors + lost
            sum += score

        case "B":
            if y == "X":
                score = rock + lost
            elif y == "Y":
                score = paper + draw
            else:
                score = scissors + won
            sum += score

        case "C":
            if y == "X":
                score = rock + won
            elif y == "Y":
                score = paper + lost
            else:
                score = scissors + draw
            sum += score'''
    # part 2
    match y:
        case "X":
            if x == "A":
                score = scissors
            elif x == "B":
                score = rock
            else:
                score = paper
            sum += score

        case "Y":
            if x == "A":
                score = draw + rock
            elif x == "B":
                score = draw + paper
            else:
                score = draw + scissors
            sum += score

        case "Z":
            if x == "A":
                score = won + paper
            elif x == "B":
                score = won + scissors
            else:
                score = won + rock
            sum += score
print(sum)

''' X means you need to lose
    Y means you need to draw
    Z means you need to win  '''
