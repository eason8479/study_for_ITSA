turn = int(input())

current_pos = [-99999, -99999, 99999, 99999]

for _ in range (turn):
    input_pos = [int(i) for i in input().split()]

    if (input_pos[0] > current_pos[0]):
        current_pos[0] = input_pos[0]

    if (input_pos[1] > current_pos[1]):
        current_pos[1] = input_pos[1]

    if (input_pos[2] < current_pos[2]):
        current_pos[2] = input_pos[2]

    if (input_pos[3] < current_pos[3]):
        current_pos[3] = input_pos[3]

print ((current_pos[3] - current_pos[1]) * (current_pos[2] - current_pos[0]))
