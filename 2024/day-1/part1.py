list1, list2 = [], []
with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

list1.sort()
list2.sort()

distance = 0
for index in range(len(list1)):
    distance += abs(list1[index] - list2[index])
print(distance)

