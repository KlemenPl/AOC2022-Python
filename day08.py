from shared import get_input

lines = get_input(8)

board = lines[:-1]
board = [[int(el) for el in row] for row in board]

BOARD_SIZE_Y = len(board)
BOARD_SIZE_X = len(board[0])


def is_visible(x, y, dX, dY):
    initialX = x
    initialY = y
    x += dX
    y += dY
    while 0 <= x < BOARD_SIZE_X and 0 <= y < BOARD_SIZE_Y:
        if board[initialY][initialX] <= board[y][x]:
            return False
        x += dX
        y += dY
    return True


count = 0
count_max = 0
for y, row in enumerate(board):
    for x, el in enumerate(row):
        if is_visible(x, y, 1, 0) or \
                is_visible(x, y, 0, 1) or \
                is_visible(x, y, -1, 0) or \
                is_visible(x, y, 0, -1):
            count += 1

print("Part 1:", count)


def get_visible_dist(x, y, dX, dY):
    initialX = x
    initialY = y
    dist = 0
    x += dX
    y += dY
    while 0 <= x < BOARD_SIZE_X and 0 <= y < BOARD_SIZE_Y:
        if board[initialY][initialX] <= board[y][x]:
            return dist + 1
        x += dX
        y += dY
        dist += 1
    return dist


count_max = 0
for y, row in enumerate(board):
    for x, el in enumerate(row):
        left = get_visible_dist(x, y, -1, 0)
        right = get_visible_dist(x, y, 1, 0)
        up = get_visible_dist(x, y, 0, 1)
        down = get_visible_dist(x, y, 0, -1)
        count = left * right * up * down
        count_max = max(count_max, count)

print("Part 2:", count_max)
