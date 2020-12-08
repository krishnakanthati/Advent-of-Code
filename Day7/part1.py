file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()
li = []

# for i in inputs_in_file:
#     li.append(i[:i.index('bags') - 1])

# print(li)

for i in inputs_in_file:
    li.append(i[i.index('contain'):])
print(li)
