with open('../input.txt') as file:
    lines = [line.rstrip() for line in file]

sum = 0


def evaluate(sol, numbers):
    if len(numbers) == 1:
        return sol == numbers[0]
    return (evaluate(sol, [numbers[0] + numbers[1]] + numbers[2:]) or evaluate(sol, [numbers[0] * numbers[1]] + numbers[2:]))


for line in lines:
    index = line.index(':')
    sol = line[:index]
    sol = int(sol)
    numbers = line[index + 1:].split()
    numbers = [int(x) for x in numbers]
    if evaluate(sol, numbers):
        sum += sol

print(sum)
