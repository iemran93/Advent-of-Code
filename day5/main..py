dic_ = {'1': ['B', 'Q', 'C'],
        '2': ['R', 'Q', 'W', 'Z'],
        '3': ['B', 'M', 'R', 'L', 'V'],
        '4': ['C', 'Z', 'H', 'V', 'T', 'W'],
        '5': ['D', 'Z', 'H', 'B', 'N', 'V', 'G'],
        '6': ['H', 'N', 'P', 'C', 'J', 'F', 'V', 'Q'],
        '7': ['D', 'G', 'T', 'R', 'W', 'Z', 'S'],
        '8': ['C', 'G', 'M', 'N', 'B', 'W', 'Z', 'P'],
        '9': ['N', 'J', 'B', 'M', 'W', 'Q', 'F', 'P']
        }


operations = open("day5\move.txt", "r").read().split("\n")


def task_1():
    for operation in operations:
        count = 0
        operation_lst = [i for i in operation if i.isdigit()]

        if len(operation_lst) > 3:
            range_ = int(operation_lst[0]+operation_lst[1])
            stack_a = operation_lst[2]
            stack_b = operation_lst[3]
        else:
            range_ = int(operation_lst[0])
            stack_a = operation_lst[1]
            stack_b = operation_lst[2]

        while count < range_:
            crate = dic_[stack_a][-1]
            dic_[stack_a].pop(-1)
            dic_[stack_b].append(crate)
            count += 1


def task_2():
    for operation in operations:
        count = 0
        crate_lst = []
        operation_lst = [i for i in operation if i.isdigit()]

        if len(operation_lst) > 3:
            range_ = int(operation_lst[0]+operation_lst[1])
            stack_a = operation_lst[2]
            stack_b = operation_lst[3]
        else:
            range_ = int(operation_lst[0])
            stack_a = operation_lst[1]
            stack_b = operation_lst[2]

        crate_lst = dic_[stack_a][-range_:]
        for item in crate_lst:
            dic_[stack_b].append(item)
            dic_[stack_a].pop(-1)


# task_1()
# task_2()
answer = ''
for stack in dic_.values():
    answer = answer + stack[-1]
print(answer)
