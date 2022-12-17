from shared import get_input
import time

wind = get_input(17)[0]

# Origin is bottom left corner for all shapes
SHAPE_MINUS = [(0, 0), (1, 0), (2, 0), (3, 0)]
SHAPE_PLUS = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
SHAPE_L = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
SHAPE_PIPE = [(0, 0), (0, 1), (0, 2), (0, 3)]
SHAPE_SQUARE = [(0, 0), (1, 0), (0, 1), (1, 1)]

shape_order = [SHAPE_MINUS, SHAPE_PLUS, SHAPE_L, SHAPE_PIPE, SHAPE_SQUARE]
WIDTH = 7
occupied = [0] * WIDTH
occupied_set = set([(x, 0) for x in range(WIDTH)])


def intersects(pos, shape, check_wall=False):
    for (x, y) in shape:
        new_pos = (x + pos[0], y + pos[1])
        if (check_wall and (new_pos[0] < 0 or new_pos[0] >= len(occupied))) or new_pos in occupied_set:
            return True
    return False


def print_state(pos, shape, height):
    cur_positions = set()
    for (x, y) in shape:
        cur_positions.add((x + pos[0], y + pos[1]))

    for y in range(height - 1, -1, -1):
        print('|', end='')
        for x in range(7):
            pos = (x, y)
            if pos in occupied_set:
                print('#', end='')
            elif pos in cur_positions:
                print('@', end='')
            else:
                print('.', end='')
        print('|')
    print('+-------+')


def simulate(num_iter):
    shape_idx = 0
    wind_idx = 0
    for i in range(num_iter):
        shape = shape_order[shape_idx]
        pos = (2, max(occupied) + 4)
        while 1:
            # Apply wind
            # print(pos)
            wind_dir = -1 if wind[wind_idx] == '<' else 1
            wind_idx = (wind_idx + 1) % len(wind)
            new_pos = (pos[0] + wind_dir, pos[1])
            if not intersects(new_pos, shape, True):
                pos = new_pos
            # Apply gravity
            new_pos = (pos[0], pos[1] - 1)
            if intersects(new_pos, shape):
                break
            pos = new_pos

        # Update occupied
        for (x, y) in shape:
            x += pos[0]
            y += pos[1]
            occupied_set.add((x, y))
            occupied[x] = max(occupied[x], y)

        shape_idx = (shape_idx + 1) % len(shape_order)
    return occupied_set, occupied


def part_one():
    return max(simulate(2022)[1])


def part_two():
    # TODO: Find pattern
    pass


start = time.time()
print("Part 1:", part_one())
end = time.time()
print("Took:", str(end - start), "s.\n")

start = time.time()
print("Part 2:", part_two())
end = time.time()
print("Took:", str(end - start), "s.\n")
