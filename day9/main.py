ops = {'R': [0, '+'], 'U': [1, '+'], 'L': [0, '-'], 'D': [1, '-']}
t1 = [(0, 0)]
h = [(0, 0)]
lines = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]


def touching(t, h):
    if abs(t[0] - h[0]) == 1:
        if abs(t[1]-h[1]) == 1 or t[1] == h[1]:
            return True
    if abs(t[1] - h[1]) == 1:
        if abs(t[0]-h[0]) == 1 or t[0] == h[0]:
            return True
    elif h[0] == t[0] and h[1] == t[1]:
        return True
    else:
        return False


data = open('data.txt', 'r').read().split("\n")

for line in data:
    direction = line[:1]
    steps = int(line[2:])
    operation = ops[direction][1]
    axis = ops[direction][0]
    for step in range(1, steps+1):
        if axis == 0:
            if operation == '+':
                h.append((h[-1][axis]+1, h[-1][axis+1]))
            else:
                h.append((h[-1][axis]-1, h[-1][axis+1]))
        if axis == 1:
            if operation == "+":
                h.append((h[-1][axis-1], h[-1][axis]+1))
            else:
                h.append((h[-1][axis-1], h[-1][axis]-1))
        # compare h to t
        # print(touching(t[-1], h[-1]))
        if not touching(t1[-1], h[-1]):
            # same row or col
            if t1[-1][0] == h[-1][0] or t1[-1][1] == h[-1][1]:
                if axis == 0:
                    if operation == '+':
                        t1.append((t1[-1][axis]+1, t1[-1][axis+1]))
                    else:
                        t1.append((t1[-1][axis]-1, t1[-1][axis+1]))
                if axis == 1:
                    if operation == "+":
                        t1.append((t1[-1][axis-1], t1[-1][axis]+1))
                    else:
                        t1.append((t1[-1][axis-1], t1[-1][axis]-1))
            else:  # diagonally move
                if axis == 0:
                    if operation == '+':
                        t1.append((t1[-1][axis]+1, h[-1][axis+1]))
                    else:
                        t1.append((t1[-1][axis]-1, h[-1][axis+1]))
                if axis == 1:
                    if operation == "+":
                        t1.append((h[-1][axis-1], t1[-1][axis]+1))
                    else:
                        t1.append((h[-1][axis-1], t1[-1][axis]-1))

print(len(set(t1)))
# print(h)
