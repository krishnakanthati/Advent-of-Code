file1 = open(r"inputs.txt", "r")
inputs = file1.readlines()

li = []

for i in inputs:
    i = i.replace('\n', '')
    instructions = i[:1] + ' '
    units = i[1:]
    li.append((instructions + units).split())

for i in li:
    i[1] = int(i[1])
    if i[0] == 'S' or i[0] == 'W' or i[0] == 'L':
        i[1] = i[1] * -1


NS, EW = 0, 0
x = ['E', 'S', 'W', 'N']
face = 'E'
index = 0

for i in li:
    if i[0] == 'N' or i[0] == 'S':
        NS += i[1]

    elif i[0] == 'E' or i[0] == 'W':
        EW += i[1]

    elif i[0] == 'R':
        face_index = i[1] // 90
        index += face_index
        if index < 4:
            face = x[index]

        else:
            face = x[index % 4]
            index = index % 4

    elif i[0] == 'L':
        face_index = i[1] // 90
        index += face_index

        if index > -4:
            face = x[index]

        else:
            face = x[index % 4]
            index = index % 4

    elif i[0] == 'F':

        if face == 'S':
            NS -= i[1]

        elif face == 'N':
            NS += i[1]

        elif face == 'W':
            EW -= i[1]

        elif face == 'E':
            EW += i[1]

print(abs(NS) + abs(EW))
