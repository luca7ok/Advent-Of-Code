with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

index = lines.index('')
rules = lines[:index]
updates = lines[index + 1:]

sum = 0

for update in updates:
    update = update.split(',')
    valid = True
    for i in range(0, len(update) - 1):
        for j in range(i + 1, len(update)):
            if update[j] + '|' + update[i] in rules:
                update[i], update[j] = update[j], update[i]
                valid = False
    if not valid:
        sum += int(update[len(update) // 2])

print(sum)
