with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]
count = 0


def safe(l):
    sign = None
    valid = True
    if int(l[0]) - int(l[1]) > 0:
        sign = True
    else:
        sign = False
    if not 1 <= abs(int(l[0]) - int(l[1])) <= 3:
        valid = False
    for i in range(1, len(l) - 1):
        diff = int(l[i]) - int(l[i + 1])
        if sign and diff < 0:
            valid = False
        if not sign and diff > 0:
            valid = False
        if not 1 <= abs(diff) <= 3:
            valid = False
    return valid


for line in lines:
    line = line.split()
    valid = False
    if safe(line):
        count += 1
        valid = True
    else:
        for i in range(len(line) - 1):
            new_list = line[:i] + line[i + 1:]
            if safe(new_list):
                count += 1
                valid = True
                break
        if not valid:
            new_list = line[:len(line) - 1]
            if safe(new_list):
                count += 1

print(count)
