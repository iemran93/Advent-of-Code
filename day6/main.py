s = open("day6\input.txt", "r").read()


def task_1(s):
    for i in range(len(s)):
        if len(set(s[i:4+i])) == 4:
            print(s[i:4+i])
            print(i+4)
            break


def task_2(s):
    for i in range(len(s)):
        if len(set(s[i:14+i])) == 14:
            print(s[i:14+i])
            print(i+14)
            break


task_1(s=s)
task_2(s=s)
