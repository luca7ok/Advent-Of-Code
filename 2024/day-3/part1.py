with open('../input.txt') as file:
    text = file.read()
index = text.find('mul(')
sum = 0
while index != -1:
    start = index
    index += 4
    num1 = 0
    num2 = 0
    ok = True
    while text[index] != ',' and ok:
        try:
            num1 = num1 * 10 + int(text[index])
        except:
            ok = False
        index += 1
    if ok:
        index += 1
        while text[index] != ')' and ok:
            try:
                num2 = num2 * 10 + int(text[index])
            except:
                ok = False
            index += 1
        if ok:
            sum += num1 * num2
    index = text.find('mul(', start + 1)
print(sum)
