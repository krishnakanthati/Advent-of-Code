file1 = open(r"inputs.txt", "r")

inputs_in_file = file1.readlines()
file1.close()

count = 0

for i in inputs_in_file:

    range1 = int(i.split(' ')[0].split('-')[0])
    range2 = int(i.split(' ')[0].split('-')[1])

    char_in_password = i.split(' ')[1].split(':')[0]
    password = i.split(' ')[2]

    if password.count(char_in_password) in range(range1, range2 + 1):
        count += 1

print(count)
