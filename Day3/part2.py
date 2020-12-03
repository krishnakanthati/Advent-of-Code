file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()
file1.close()

# 323 inputs in file
grid = []

# i[:31] neglects newline character
for i in inputs_in_file:
    grid.append(i[:31] * 100)


def slope(right, down):
    count = 0
    n = 1

    # right * n gives the position
    for i in grid[down::down]:
        if i[right * n] == '#':
            count += 1
        n += 1
    return count


print(slope(1, 1) * slope(3, 1) * slope(7, 1) * slope(5, 1) * slope(1, 2))
