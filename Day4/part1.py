file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()
count = 0


for i in inputs_in_file:
    if len(inputs_in_file):
        string = ''.join(inputs_in_file[: inputs_in_file.index('\n')])

        byr = 'byr:' in string
        iyr = 'iyr:' in string
        eyr = 'eyr:' in string
        hgt = 'hgt:' in string
        hcl = 'hcl:' in string
        ecl = 'ecl:' in string
        pid = 'pid:' in string
        cid = 'cid:' in string

        x = byr and iyr and eyr and hgt and hcl and ecl and pid

        if x:
            count += 1

        inputs_in_file = inputs_in_file[inputs_in_file.index('\n') + 1:]

print(count)
