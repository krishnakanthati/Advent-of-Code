file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()

li = []
acc = 0

for i in inputs_in_file:
    i = i.replace('\n', '').split()
    i[1] = int(i[1])
    li.append(i)

for i in li:

    if i[0] == 'nop':
        i[0] = 'jmp'
        i[1] = 1

dic = dict()
n = 0
instructions = []

for i in li:
    dic.update({n: i})
    n += 1

x = 0

while True:
    if dic[x][0] == 'acc':
        acc += dic[x][1]
        instructions.append(x)
        x += 1
    else:
        x = dic[x][1] + x
        if x in instructions:
            break
        instructions.append(x)

print(instructions)
