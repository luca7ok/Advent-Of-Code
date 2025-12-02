with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

n = len(lines)
m = len(lines[0])
sum = 0


def in_grid(x, y):
    return x >= 0 and y >= 0 and x < n and y < m


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = []
end = set()


def dfs(x, y):
    global count
    global ok
    visited.append((x, y))
    if lines[x][y] == '9':
        end.add((x, y))
        ok = True
    else:
        for k in range(4):
            if (in_grid(x + dx[k], y + dy[k])
                    and (x + dx[k], y + dy[k]) not in visited
                    and int(lines[x + dx[k]][y + dy[k]]) == int(lines[x][y]) + 1):
                dfs(x + dx[k], y + dy[k])


def dfs2(x, y):
    global count
    visited.append((x, y))
    if x == xe and y == ye:
        count += 1
    else:
        for k in range(4):
            if (in_grid(x + dx[k], y + dy[k])
                    and (x + dx[k], y + dy[k]) not in visited
                    and int(lines[x + dx[k]][y + dy[k]]) == int(lines[x][y]) + 1):
                dfs2(x + dx[k], y + dy[k])
    visited.remove((x, y))

for i in range(n):
    for j in range(m):
        if lines[i][j] == '0':
            visited = []
            ok = False
            dfs(i, j)
            if ok:
                start.append((i, j))

for (xe, ye) in end:
    for (xs, ys) in start:
        count = 0
        visited = []
        dfs2(xs, ys)
        sum += count

print(sum)
