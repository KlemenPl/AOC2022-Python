from shared import get_input


def clamp(x: int) -> int:
    return max(-1, min(1, x))


lines = get_input(14)[:-1]

AIR = 0
ROCK = 1
SAND = 2

START_X = 1000
START_Y = 0
SIZE_X = 0
SIZE_Y = 0

paths = []
for line in lines:
    parts = line.split(" -> ")
    path = []
    for pos in parts:
        pos_x, pos_y = int(pos.split(",")[0]), int(pos.split(",")[1])
        path.append((pos_x, pos_y))
        START_X = min(START_X, pos_x - 1)
        SIZE_X = max(SIZE_X, pos_x + 1)
        SIZE_Y = max(SIZE_Y, pos_y + 1)
    paths.append(path)

SAND_START_X = 500 - START_X
SAND_START_Y = 0
SIZE_X -= START_X
SIZE_Y -= START_Y


def create_world():
    world = [[AIR for x in range(SIZE_X)][:] for y in range(SIZE_Y)]

    for path in paths:
        for from_pos, to_pos in zip(path, path[1:]):
            from_x, from_y = from_pos
            to_x,  to_y = to_pos
            from_x -= START_X
            to_x -= START_X
            from_y -= START_Y
            to_y -= START_Y
            d_x = clamp(to_x - from_x)
            d_y = clamp(to_y - from_y)
            while from_x != to_x or from_y != to_y:
                world[from_y][from_x] = ROCK
                from_x += d_x
                from_y += d_y
            world[from_y][from_x] = ROCK
    return world


def print_state():
    for y in range(0, SIZE_Y):
        for x in range(SIZE_X):
            state = world[y][x]
            if state == AIR:
                print(".",end='')
            elif state == ROCK:
                print("#",end='')
            else:
                print("O", end='')
        print()


iteration = 0
in_abyss = False
world = create_world()
# print_state()

while not in_abyss:
    sand_x = SAND_START_X
    sand_y = SAND_START_Y
    while 1:
        # Check, for abyss conditions
        if sand_x < 0 or sand_x > SIZE_X or sand_y + 1 >= SIZE_Y:
            in_abyss = True
            break
        # Down
        if world[sand_y + 1][sand_x] == AIR:
            sand_y += 1
        # Left
        elif world[sand_y + 1][sand_x - 1] == AIR:
            sand_x -= 1
            sand_y += 1
        # Right
        elif world[sand_y + 1][sand_x + 1] == AIR:
            sand_x += 1
            sand_y += 1
        # Stuck
        else:
            world[sand_y][sand_x] = SAND
            break
    iteration += 1


print("Part 1:", iteration - 1)

world = create_world()
SIZE_Y += 2
world.append([AIR] * SIZE_X)
world.append([ROCK] * SIZE_X)
# print_state()

iteration = 0
is_full = False
while not is_full:
    sand_x = SAND_START_X
    sand_y = SAND_START_Y
    while 1:
        # Check if full
        if world[sand_y][sand_x] == SAND:
            is_full = True
            break

        # Check, if needs expanding
        EXPAND_RATIO = 10
        if sand_x <= 0:
            SAND_START_X += EXPAND_RATIO
            sand_x += EXPAND_RATIO
            SIZE_X += EXPAND_RATIO
            world = [([AIR] * EXPAND_RATIO) + row for row in world]
            world[-1] = [ROCK] * SIZE_X
        elif sand_x + 1 >= SIZE_X:
            SIZE_X += EXPAND_RATIO
            world = [row + ([AIR] * EXPAND_RATIO) for row in world]
            world[-1] = [ROCK] * SIZE_X

        # Down

        if world[sand_y + 1][sand_x] == AIR:
            sand_y += 1
        # Left
        elif world[sand_y + 1][sand_x - 1] == AIR:
            sand_x -= 1
            sand_y += 1
        # Right
        elif world[sand_y + 1][sand_x + 1] == AIR:
            sand_x += 1
            sand_y += 1
        # Stuck
        else:
            world[sand_y][sand_x] = SAND
            break
    iteration += 1

print("Part 2:", iteration - 1)