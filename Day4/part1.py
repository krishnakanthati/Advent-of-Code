file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()

count = 0

for i in inputs_in_file:
    if len(inputs_in_file):
        string = ''.join(inputs_in_file[: inputs_in_file.index('\n')])

        string = string.replace('\n', ' ').split()

        dic = {}

        for i in string:
            dic.update({i.split(':')[0]: i.split(':')[1]})
        # print(dic)

        byr = dic.get('byr')
        iyr = dic.get('iyr')
        eyr = dic.get('eyr')
        hgt = dic.get('hgt')
        hcl = dic.get('hcl')
        ecl = dic.get('ecl')
        pid = dic.get('pid')

        x = byr and iyr and eyr and hgt and hcl and ecl and pid

        if x:
            count += 1

        inputs_in_file = inputs_in_file[inputs_in_file.index('\n') + 1:]

print(count)
