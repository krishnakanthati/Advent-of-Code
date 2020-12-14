file1 = open(r"inputs.txt", "r")
inputs = file1.readlines()
li = []

for i in inputs:
    i = int(i.replace('\n', ''))
    li.append(i)

b = 25
a = 0

z = []


while len(li[a: b]) != 24:
    for i in li[a: b]:
        for n in li[a: b - 1]:
            try:
                if (i + n) == li[b] and li[b] not in z:
                    z.append(li[b])
            except IndexError:
                pass

    a += 1
    b += 1


for i in li[25:]:
    if i not in z:
        break
print(i)
