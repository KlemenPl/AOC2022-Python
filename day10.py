from shared import get_input

lines = get_input(10)[:-1]


class Data:
    cycle = 0
    reg_x = 1
    adding = 0
    rows = [[0 for x in range(40)] for y in range(6)]
    sum_strength = 0


data = Data()

for line in lines:
    def tick(data: Data):
        data.cycle += 1
        if data.cycle in [20, 60, 100, 140, 180, 220]:
            data.sum_strength += data.cycle * data.reg_x
        idx = (data.cycle - 1) // 40
        pos = (data.cycle - 1) % 40
        sprite_pos = data.reg_x
        dif = abs(sprite_pos - pos)
        data.rows[idx][pos] = dif <= 1


    if line == "noop":
        tick(data)
    else:
        tick(data)
        tick(data)
        data.reg_x += int(line.split()[1])

print("Part 1:", data.sum_strength)
print("Part 2:")
for row in data.rows:
    for column in row:
        if column:
            print("#", end='')
        else:
            print(".", end='')
    print()
