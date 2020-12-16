index = 0
x = ['E', 'S', 'W', 'N']

instructions = 'L'

# while instructions == 'R':

#     face_index = int(input())
#     index += face_index
#     if index < 4:
#         print(x[index])

#     else:
#         print(x[index % 4])
#         index = index % 4


while instructions == 'L':

    face_index = int(input())
    index += face_index
    if index > -4:
        print(x[index])

    else:
        print(x[index % 4])
        index = index % 4
