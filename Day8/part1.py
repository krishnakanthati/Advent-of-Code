file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()

li = []
acc = 0

for i in inputs_in_file:
    i = i.replace('\n', '').split()
    i[1] = int(i[1])
    li.append(i)

dic = dict()
n = 0
instructions = []

for i in li:
    dic.update({n: i})
    n += 1

# x is the current index of the list li
x = 0

while True:
    if dic[x][0] == 'acc':
        if x in instructions:
            break

        acc += dic[x][1]
        instructions.append(x)
        x += 1

    elif dic[x][0] == 'jmp':
        x = dic[x][1] + x
    else:
        x += 1

print(acc)
