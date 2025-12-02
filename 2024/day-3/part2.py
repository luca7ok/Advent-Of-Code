with open('../input.txt') as file:
    text = file.read()

sum = 0
index = text.find('mul(')
index_do = text.find('do()')
index_dont = text.find("don't()")
while index != -1:
    if index_dont ==-1 or index < index_dont:
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
    else:
        index_do = text.find('do()', index_dont + 1)
        if index_do != -1:
            index = text.find('mul(', index_do + 1)
            index_dont = text.find("don't()", index_do + 1)
        else:
            index = -1
print(sum)
