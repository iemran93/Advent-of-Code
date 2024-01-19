with open("./2023/day3/input.txt") as file:
    content = file.readlines()

content = [line.strip("\n") for line in content]

rows = len(content)
columns = len(content[0])
gearPos = {}


def getNum(row, col):
    fstIndx = col
    lstIndx = fstIndx+1
    while lstIndx < columns and content[row][lstIndx].isdigit():
        lstIndx += 1
    num = content[row][fstIndx:lstIndx]
    return num, fstIndx, lstIndx


def checkAround(row, fstIndx, lstIndx):
    # Check Right
    if lstIndx != columns:
        if content[row][lstIndx] != "." and not content[row][lstIndx].isdigit():
            character = content[row][lstIndx]
            if character == "*":
                return True, str(row)+str(lstIndx)
    # Check Left
    if fstIndx != 0:
        if content[row][fstIndx-1] != "." and not content[row][fstIndx-1].isdigit():
            character = content[row][fstIndx-1]
            if character == "*":
                return True, str(row)+str(fstIndx-1)
    # Check above
    if row != 0:
        if fstIndx != 0:
            above = content[row-1][fstIndx-1:lstIndx+1]
            col = fstIndx-1
        else:
            above = content[row-1][fstIndx:lstIndx+1]
            col = fstIndx
        for point in above:
            if point != "." and not point.isdigit():
                character = point
                if character == "*":
                    return True, str(row-1)+str(col)
            col += 1
    # Check down
    if row != rows-1:
        if fstIndx != 0:
            down = content[row+1][fstIndx-1:lstIndx+1]
            col = fstIndx-1
        else:
            down = content[row+1][fstIndx:lstIndx+1]
            col = fstIndx
        for point in down:
            if point != "." and not point.isdigit():
                character = point
                if character == "*":
                    return True, str(row+1)+str(col)
            col += 1
    return False, None


for row in range(rows):
    col = 0
    while col < columns:
        point = content[row][col]
        if point.isdigit():
            num, fstIndx, lstIndx = getNum(row, col)
            found, pos = checkAround(row, col, lstIndx)
            if found:
                if pos not in gearPos or gearPos[pos] is None:
                    gearPos[pos] = [num]
                else:
                    gearPos[pos].append(num)
            col += (lstIndx-fstIndx)
        else:
            col += 1

sumOfPairs = 0
sus = 0
for k, v in gearPos.items():
    if len(v) == 2:
        sus += 1
        sumOfPairs += int(v[0]) * int(v[1])
print(sus)
