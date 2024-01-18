with open("./2023/day3/input.txt") as file:
    content = file.readlines()

content = [line.strip("\n") for line in content]

rows = len(content)
columns = len(content[0])


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
            return True
    # Check Left
    if fstIndx != 0:
        if content[row][fstIndx-1] != "." and not content[row][fstIndx-1].isdigit():
            return True
    # Check above
    if row != 0:
        if fstIndx != 0:
            above = content[row-1][fstIndx-1:lstIndx+1]
        else:
            above = content[row-1][fstIndx:lstIndx+1]
        for point in above:
            if point != "." and not point.isdigit():
                return True
    # Check down
    if row != rows-1:
        if fstIndx != 0:
            down = content[row+1][fstIndx-1:lstIndx+1]
        else:
            down = content[row+1][fstIndx:lstIndx+1]
        for point in down:
            if point != "." and not point.isdigit():
                return True
        return False


numsToCount = []
for row in range(rows):
    col = 0
    while col < columns:
        point = content[row][col]
        if point.isdigit():
            num, fstIndx, lstIndx = getNum(row, col)
            if checkAround(row, col, lstIndx):
                numsToCount.append(int(num))
            col += (lstIndx-fstIndx)
        else:
            col += 1

print(numsToCount, sum(numsToCount))
