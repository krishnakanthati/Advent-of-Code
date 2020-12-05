import re

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

        def byr(byr):
            if (byr != None) and (int(byr) in range(1920, 2003)):
                return True
            else:
                return False

        def iyr(iyr):
            if (iyr != None) and (int(iyr) in range(2010, 2021)):
                return True
            else:
                return False

        def eyr(eyr):
            if (eyr != None) and (int(eyr) in range(2020, 2031)):
                return True
            else:
                return False

        def hgt(hgt):
            if hgt != None:
                if hgt[-2:] == 'cm':
                    if int(hgt[:-2]) in range(150, 194):
                        return True
                    else:
                        return False
                elif hgt[-2:] == 'in':
                    if int(hgt[:-2]) in range(59, 77):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False

        def hcl(hcl):
            if hcl != None:
                if len(hcl) == 7 and re.compile(r"^#[0-9a-f]{6}").match(hcl):
                    return True
                else:
                    return False
            else:
                return False

        def ecl(ecl):
            if ecl != None:
                if len(ecl) == 3 and re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)").match(ecl):
                    return True
                else:
                    return False
            else:
                return False

        def pid(pid):
            if pid != None:
                if len(pid) == 9 and re.compile(r"^[0-9]{9}").match(pid):
                    return True
                else:
                    return False
            else:
                return False

        x = byr(dic.get('byr')) and iyr(dic.get('iyr')) and eyr(dic.get('eyr')) and hgt(dic.get('hgt')) and hcl(dic.get('hcl')) and ecl(
            dic.get('ecl')) and pid(dic.get('pid'))

        if x:
            count += 1

        inputs_in_file = inputs_in_file[inputs_in_file.index('\n') + 1:]

print(count)
