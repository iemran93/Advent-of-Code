# Resource https://www.youtube.com/watch?v=o6KVs1EgAYk

import pandas as pd

with open("day8\data.txt", "r") as file:
    lines = file.read().split("\n")

ROWS = len(lines)
COLUMNS = len(lines[0])

edges = (COLUMNS * 2) + (ROWS * 2 - 4)
total = edges
scores = []

for row in range(1, ROWS-1):
    for col in range(1, COLUMNS-1):
        tree = lines[row][col]

        right = [lines[row][col+i] for i in range(1, COLUMNS-col)]
        left = [lines[row][col-i] for i in range(1, col+1)]
        up = [lines[row-i][col] for i in range(1, row+1)]
        down = [lines[row+i][col] for i in range(1, ROWS-row)]

        if max(right) < tree or max(left) < tree or max(up) < tree or max(down) < tree:
            total += 1

        score = 1
        for lst in (right, left, up, down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] >= tree:
                    tracker += 1
                    break

            score *= tracker

        scores.append(score)

print(f"the total visible trees {total}")
print(f"the highest score is {max(scores)}")
