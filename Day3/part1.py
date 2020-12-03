file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()
file1.close()

# 323 inputs in file

grid = []

for i in inputs_in_file:
    grid.append(i[:31] * 32)

count = 0
n = 1

# 3 * n gives the position
for i in grid[1::1]:
    if i[3 * n] == '#':
        count += 1
    n += 1

print(count)
