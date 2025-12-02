with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

coordinates = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '.':
            coordinates.append((lines[i][j], i, j))
count = 0
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j and coordinates[i][0] == coordinates[j][0]:
            new_x = 2 * coordinates[j][1] - coordinates[i][1]
            new_y = 2 * coordinates[j][2] - coordinates[i][2]
            if new_x >= 0 and new_y >= 0 and new_y < len(lines[0]) and new_x < len(lines):
                if lines[new_x][new_y] != '#':
                    count += 1
                    lines[new_x] = lines[new_x][:new_y] + '#' + lines[new_x][new_y + 1:]

print(count)

