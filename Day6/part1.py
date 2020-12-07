file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()

count = 0

for i in inputs_in_file:
    if len(inputs_in_file):
        string = ''.join(inputs_in_file[: inputs_in_file.index('\n')])

        string = string.replace('\n', '')
        # print(string)

        ans = ""
        for i in string:
            if(i in ans):
                pass
            else:
                ans = ans+i

        count += len(ans)

        inputs_in_file = inputs_in_file[inputs_in_file.index('\n') + 1:]

print(count)
