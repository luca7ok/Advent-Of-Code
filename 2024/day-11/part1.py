with open('../input.txt') as file:
    text = file.read()

text = text.split()
sol = []
for i in range(75):
    print(i)
    for j in range(len(text)):
        if text[j][0] == '0':
            sol.append('1')
        elif len(text[j]) % 2 == 0:
            sol.append(str(int(text[j][:len(text[j]) // 2])))
            sol.append(str(int(text[j][len(text[j]) // 2:])))
        else:
            sol.append(str(int(text[j]) * 2024))
    text = sol[:]
    sol = []

print(len(text))
