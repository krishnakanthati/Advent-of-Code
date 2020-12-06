import math

file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()

seat_id = []


def boarding_pass(code):

    row_li = list(range(0, 128))
    col_li = list(range(0, 8))

    row = code[:-3]
    col = code[-3:]

    while len(row_li) != 1:
        for i in row:
            mi = math.ceil(row_li.index(row_li[-1]) / 2)
            if i == 'F':
                row_li = row_li[: mi]
            if i == 'B':
                row_li = row_li[mi:]
    else:
        r = int(''.join(map(str, row_li)))

    while len(col_li) != 1:
        for i in row:
            mi = math.ceil(col_li.index(col_li[-1]) / 2)
            if i == 'L':
                col_li = col_li[: mi]
            if i == 'R':
                col_li = col_li[mi:]
    else:
        c = int(''.join(map(str, col_li)))

    return r * 8 + c


for i in inputs_in_file:
    seat_id.append(boarding_pass(i))

print(max(seat_id))
