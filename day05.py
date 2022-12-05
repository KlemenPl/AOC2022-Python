from shared import get_input

lines = get_input(5)

idx = lines.index('')
setup = lines[:idx]
lines = lines[idx + 1:]

STACK_SIZE = 9


def read_setup(setup):
    stacks = [[] for i in range(STACK_SIZE)]

    for line in setup[:-1:][::-1]:
        idx = 0
        for create in line[1::4]:
            if create != ' ':
                stacks[idx].append(create)
            idx += 1
    return stacks


stacks = read_setup(setup)

for line in lines[:-1:]:
    line = line.split()
    amount = int(line[1])
    from_stack = int(line[3]) - 1
    to_stack = int(line[5]) - 1

    for i in range(amount):
        stacks[to_stack].append(stacks[from_stack].pop())

print("Part 1: ", end='')
for i in range(STACK_SIZE):
    print(stacks[i][-1], end='')
print()


stacks = read_setup(setup)

for line in lines[:-1:]:
    line = line.split()
    amount = int(line[1])
    from_stack = int(line[3]) - 1
    to_stack = int(line[5]) - 1

    temp = []
    for i in range(amount):
        temp.append(stacks[from_stack].pop())
    while temp:
        stacks[to_stack].append(temp.pop())

print("Part 2: ", end='')
for i in range(STACK_SIZE):
    print(stacks[i][-1], end='')
print()
