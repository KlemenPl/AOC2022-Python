import time
from shared import get_input

lines = get_input(18)[:-1]

blocks = set()

for block in lines:
    x, y, z = map(int, block.split(','))
    blocks.add((x, y, z))

SIDES = [
    (0, 0, 1),
    (0, 0, -1),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
]


def part_one():
    num_sides = 0
    for block in lines:
        x, y, z = map(int, block.split(','))
        for side in SIDES:
            side = (side[0] + x, side[1] + y, side[2] + z)
            if side not in blocks:
                num_sides += 1
    return num_sides


def part_two():
    # Map outside
    # Mapping out only 1 block outside would be way more efficient, but this works good enough
    LIMIT = 64
    outside = set()
    q = [(-1, -1, -1)]
    while q:
        pos = q.pop()
        if pos in outside:
            continue
        outside.add(pos)

        for side in SIDES:
            side = (side[0] + pos[0], side[1] + pos[1], side[2] + pos[2])
            if side[0] < -1 or side[0] >= LIMIT or side[1] < -1 or side[1] >= LIMIT or side[2] < -1 or side[2] >= LIMIT:
                continue

            if side not in outside and side not in blocks:
                q.append(side)

    num_sides = 0
    for block in lines:
        x, y, z = map(int, block.split(','))
        for side in SIDES:
            side = (side[0] + x, side[1] + y, side[2] + z)
            if side in outside:
                num_sides += 1
    return num_sides


start = time.time()
print("Part 1:", part_one())
end = time.time()
print("Took:", str(end - start), "s.\n")

start = time.time()
print("Part 2:", part_two())
end = time.time()
print("Took:", str(end - start), "s.\n")
