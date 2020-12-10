file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()

li = []

for i in inputs_in_file:
    i = i.replace('\n', '').split()
    i[1] = int(i[1])
    li.append(i)


def d():
    dic = dict()
    n = 0
    for i in li:
        dic.update({n: i})
        n += 1
    return dic


def control(dic):

    x = 0
    acc = 0
    instructions = []
    while True:

        if x == len(dic):
            return print(acc)
        elif x > len(dic):
            return None

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


for i in li:
    if i[0] == 'nop' and i[1] == 0:
        li.remove(i)

for i in li:
    if i[0] == 'nop' and i[1] != 0:
        i[0] = 'jmp'

        if control(d()) == None:
            i[0] = 'nop'
        else:
            control(d())
            break

    elif i[0] == 'jmp':
        i[0] = 'nop'

        if control(d()) == None:
            i[0] = 'jmp'

        else:
            control(d())
            break
