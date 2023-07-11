# resource https://github.com/0xJFFRY/AdventOfCode-2022/blob/main/day7.py

data = open("day7\input.txt", "r").read()
lines = [x for x in data.split("\n")]

path = "/home"
dirs = {"/home": 0}

for line in lines:
    command = line.split()

    if command[0] == "$":

        if command[1] == "ls":
            pass

        if command[1] == "cd":
            if command[2] == "/":
                path = "/home"
            elif command[2] == "..":
                path = path[:path.rfind("/")]
            else:
                dir_name = command[2]
                path = path + "/" + dir_name
                dirs.update({path: 0})

    elif command[0] == "dir":
        pass

    else:
        size = int(command[0])
        dir = path
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]

count = 0
ntf = 30000000 - (70000000 - dirs['/home'])
ntf_lst = []

for k, v in dirs.items():
    if v <= 100000:
        count += v
    if v >= ntf:
        ntf_lst.append(v)

print(f"Part one: {count}")
print(f"Part two: {min(ntf_lst)}")
