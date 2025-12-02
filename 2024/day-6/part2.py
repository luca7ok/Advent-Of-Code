with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

n = len(lines)
m = len(lines[0])

visited = [[4] * m for i in range(n)]
visited2 = [[[] for _ in range(100)] * m for i in range(n)]

kx = [-1, 0, 1, 0]
ky = [0, 1, 0, -1]
k = 0

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            x_coord = i
            y_coord = j
            break
og_x = x_coord
og_y = y_coord
count = 0

visited2[og_x][og_y].append(0)
while not (x_coord == 0 or y_coord == 0 or x_coord == n - 1 or y_coord == m - 1):
    x_coord += kx[k]
    y_coord += ky[k]
    if lines[x_coord][y_coord] == '#':
        x_coord -= kx[k]
        y_coord -= ky[k]
        k = (k + 1) % 4
    else:
        visited[x_coord][y_coord] = k

for i in range(n):
    for j in range(m):
        if visited[i][j]!=4 and (i != og_x and j != og_y):
            lines[i] = lines[i][:j] + '#' + lines[i][j + 1:]
            x_coord = og_x
            y_coord = og_y
            k = 0
            visited2 = [[[] for _ in range(100)] * m for i in range(n)]
            while not (x_coord == 0 or y_coord == 0 or x_coord == n - 1 or y_coord == m - 1):
                x_coord += kx[k]
                y_coord += ky[k]
                if lines[x_coord][y_coord] == '#':
                    x_coord -= kx[k]
                    y_coord -= ky[k]
                    k = (k + 1) % 4
                    if k in visited2[x_coord][y_coord]:
                        count += 1
                        break
                    else:
                        visited2[x_coord][y_coord].append(k)
                else:
                    if k in visited2[x_coord][y_coord]:
                        count += 1
                        break
                    else:
                        visited2[x_coord][y_coord].append(k)
            lines[i] = lines[i][:j] + '.' + lines[i][j + 1:]

print(count)
