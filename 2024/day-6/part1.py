with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

n = len(lines)
m = len(lines[0])

visited = [[False] * m for i in range(n)]

kx = [-1, 0, 1, 0]
ky = [0, 1, 0, -1]
k = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            x_coord = i
            y_coord = j
            break

count = 0
while not (x_coord == 0 or y_coord == 0 or x_coord == n - 1 or y_coord == m - 1):
    x_coord += kx[k]
    y_coord += ky[k]
    if lines[x_coord][y_coord] == '#':
        x_coord -= kx[k]
        y_coord -= ky[k]
        k = (k + 1) % 4
    else:
        if not visited[x_coord][y_coord]:
            count += 1
        visited[x_coord][y_coord] = True
        # lines[x_coord] = lines[x_coord][:y_coord] + 'X' + lines[x_coord][y_coord + 1:]

print(count + 1)
