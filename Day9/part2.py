file1 = open(r"inputs.txt", "r")
inputs = file1.readlines()
li = []

for i in inputs:
    i = int(i.replace('\n', ''))
    li.append(i)

b = 1
a = 0

while True:
    if sum(li[a: b]) == 731031916:
        print(min(li[a: b]) + max(li[a: b]))
        break
    elif sum(li[a: b]) > 731031916:
        a += 1
        b = a + 1

    b += 1
