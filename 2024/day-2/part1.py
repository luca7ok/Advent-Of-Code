with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]
count = 0
for line in lines:
    line = line.split()
    sign = None
    valid = True
    if int(line[0]) - int(line[1]) > 0:
        sign = True
    else:
        sign = False
    if not 1 <= abs(int(line[0]) - int(line[1])) <= 3:
        valid = False
    for i in range(1, len(line) - 1):
        diff = int(line[i]) - int(line[i + 1])
        if sign and diff < 0:
            valid = False
        if not sign and diff > 0:
            valid = False
        if not 1 <= abs(diff) <= 3:
            valid = False
    if valid:
        count += 1
print(count)
