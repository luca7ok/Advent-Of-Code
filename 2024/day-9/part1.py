from collections import deque

with open('../input.txt') as file:
    text = file.read()

blocks = deque([])
spaces = deque([])
sol = []
id = 0
pos = 0
sum = 0
for i, b in enumerate(text):
    if i % 2 == 0:
        for _ in range(int(b)):
            blocks.append((pos, id))
            sol.append(id)
            pos += 1
        id += 1
    else:
        for _ in range(int(b)):
            spaces.append(pos)
            sol.append(None)
            pos += 1
size = len(blocks)
sol = sol[:size]
while blocks[-1][0] > spaces[0]:
    sol[spaces[0]] = blocks[-1][1]
    blocks.pop()
    spaces.popleft()

for i, c in enumerate(sol):
    sum += i * c

print(sum)

