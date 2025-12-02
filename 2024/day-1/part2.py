list1, list2 = [], []
with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

score = 0
for elem in list1:
    score += list2.count(elem) * elem
print(score)
