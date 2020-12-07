file1 = open(r"inputs.txt", "r")
inputs_in_file = file1.readlines()

count = 0

for i in inputs_in_file:
    if len(inputs_in_file):
        string = ''.join(inputs_in_file[: inputs_in_file.index('\n')])

        string = string.replace('\n', ' ').split()
        first = set(string[0])

        def se(first, i):
            return first & i

        for i in string[1:]:
            first = se(first, set(i))

        count += len(first)

        inputs_in_file = inputs_in_file[inputs_in_file.index('\n') + 1:]

print(count)
