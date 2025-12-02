with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

n = len(lines)
m = len(lines[0])
sum = 0

def in_grid(x, y):
    return x >= 0 and y >= 0 and x < n and y < m


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global count
    visited.append((x, y))
    if lines[x][y] == '9':
        count += 1
    else:
        for k in range(4):
            if (in_grid(x + dx[k], y + dy[k])
                    and (x + dx[k], y + dy[k]) not in visited
                    and int(lines[x + dx[k]][y + dy[k]]) == int(lines[x][y]) + 1):
                dfs(x + dx[k], y + dy[k])


for i in range(n):
    for j in range(m):
        if lines[i][j] == '0':
            visited = []
            count = 0
            dfs(i, j)
            sum += count

print(sum)
