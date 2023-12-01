def replaceletter(line):
    lettodig = {"one": '1', "two": '2', "three": '3', "four": '4',
                "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    newline = ""
    i = 0
    while i < len(line):
        end = i + 3
        if line[i:end] in lettodig.keys():
            newline += lettodig[line[i:end]]
            i += 1
            continue
        end = i + 4
        if line[i:end] in lettodig.keys():
            newline += lettodig[line[i:end]]
            i += 1
            continue
        end = i + 5
        if line[i:end] in lettodig.keys():
            newline += lettodig[line[i:end]]
            i += 1
            continue
        newline += line[i]
        i += 1
    return newline


with open("data.txt", 'r') as file:
    content = file.read().split('\n')
ctotal = 0
for line in content:
    nums = []
    nline = replaceletter(line)
    for char in nline:
        if char.isdigit():
            nums.append(int(char))
    cvalues = (nums[0]*10)+nums[-1]
    ctotal += cvalues

print(ctotal)
