import pandas as pd
total_pair = 0

df = pd.read_csv("day4\input.txt")
for index, row in df.iterrows():
    state = []

    d1 = row['d1']
    d1_lst = list(map(int, d1.split("-")))
    d1_lst_range = [i for i in range(d1_lst[0], d1_lst[1]+1)]

    d2 = row['d2']
    d2_lst = list(map(int, d2.split("-")))
    d2_lst_range = [i for i in range(d2_lst[0], d2_lst[1]+1)]

    if sum(d1_lst_range) == sum(d2_lst_range):
        state.append(True)
    elif sum(d1_lst_range) > sum(d2_lst_range):
        for i in d2_lst_range:
            if i in d1_lst_range:
                state.append(True)
            else:
                state.append(False)
    else:
        for i in d1_lst_range:
            if i in d2_lst_range:
                state.append(True)
            else:
                state.append(False)

    if all(state):
        total_pair += 1
print(total_pair)
