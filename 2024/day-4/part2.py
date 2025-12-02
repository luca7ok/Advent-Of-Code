with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

count = 0
n = len(lines)
m = len(lines[0])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'A':
            if i - 1 >= 0 and j - 1 >= 0 and i + 1 < n and j + 1 < m and (
                    (lines[i - 1][j - 1] == 'M' and lines[i + 1][j + 1] == 'S') or (
                    lines[i - 1][j - 1] == 'S' and lines[i + 1][j + 1] == 'M')) and (
                    (lines[i - 1][j + 1] == 'M' and lines[i + 1][j - 1] == 'S') or (
                    lines[i - 1][j + 1] == 'S' and lines[i + 1][j - 1] == 'M')):
                count += 1

print(count)
