with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

count = 0
n = len(lines)
m = len(lines[0])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'X':
            try:
                if lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S' and i + 3 < n:
                    count += 1
            except:
                pass
            try:
                if lines[i - 1][j] == 'M' and lines[i - 2][j] == 'A' and lines[i - 3][j] == 'S' and i - 3 >= 0:
                    count += 1
            except:
                pass
            try:
                if lines[i][j + 1] == 'M' and lines[i][j + 2] == 'A' and lines[i][j + 3] == 'S' and j + 3 < m:
                    count += 1
            except:
                pass
            try:
                if lines[i][j - 1] == 'M' and lines[i][j - 2] == 'A' and lines[i][j - 3] == 'S' and j - 3 >= 0:
                    count += 1
            except:
                pass
            try:
                if lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][
                    j + 3] == 'S' and i + 3 < n and j + 3 < m:
                    count += 1
            except:
                pass
            try:
                if lines[i - 1][j + 1] == 'M' and lines[i - 2][j + 2] == 'A' and lines[i - 3][
                    j + 3] == 'S' and i - 3 >= 0 and j + 3 < m:
                    count += 1
            except:
                pass
            try:
                if lines[i - 1][j - 1] == 'M' and lines[i - 2][j - 2] == 'A' and lines[i - 3][
                    j - 3] == 'S' and i - 3 >= 0 and j - 3 >= 0:
                    count += 1
            except:
                pass
            try:
                if lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S' and i+3<n and j-3>=0:
                    count += 1
            except:
                pass
print(count)
