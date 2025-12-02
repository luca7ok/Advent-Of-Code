with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

count = 0
coordinates = []
set = set()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] != '.':
            coordinates.append((lines[i][j], i, j))
            set.add(lines[i][j])
for x in set:
    num = 0
    for i in range(len(coordinates)):
        if coordinates[i][0] == x:
            num += 1
    if num != 1:
        count += num


def in_grid(x, y):
    return x >= 0 and y >= 0 and y < len(lines[0]) and x < len(lines)


for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j and coordinates[i][0] == coordinates[j][0]:
            x = coordinates[i][1]
            y = coordinates[i][2]
            mid_x = coordinates[j][1]
            mid_y = coordinates[j][2]
            sym_x = 2 * mid_x - x
            sym_y = 2 * mid_y - y
            while in_grid(sym_x, sym_y):
                if lines[sym_x][sym_y] == '.':
                    count += 1
                    lines[sym_x] = lines[sym_x][:sym_y] + '#' + lines[sym_x][sym_y + 1:]
                x = mid_x
                y = mid_y
                mid_x = sym_x
                mid_y = sym_y
                sym_x = 2 * mid_x - x
                sym_y = 2 * mid_y - y

print(count)
