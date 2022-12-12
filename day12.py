from shared import get_input
from heapq import *

lines = get_input(12)[:-1]

start = (0, 0)
end = (0, 0)

maze = [[ord(c) for c in line] for line in lines]

SIZE_X = len(maze[0])
SIZE_Y = len(maze)


def get_elevation(node):
    return maze[node[1]][node[0]]


def in_maze(node):
    return 0 <= node[0] < SIZE_X and 0 <= node[1] < SIZE_Y


for y, row in enumerate(maze):
    for x, c in enumerate(row):
        if c == ord('S'):
            start = (x, y)
            maze[y][x] = ord('a')
        elif c == ord('E'):
            end = (x, y)
            maze[y][x] = ord('z')

moves = [
    (-1, 0),  # Left
    (1, 0),  # Right
    (0, 1),  # Up
    (0, -1),  # Down
]

heap = []
heappush(heap, (0, 0, start))
visited = set()

while heap:
    cost, path_count, node = heappop(heap)

    if node == end:
        print("Part 1:", path_count)
        break

    for move in moves:
        new_node = (move[0] + node[0], move[1] + node[1])
        if new_node in visited:
            continue
        if not in_maze(new_node):
            continue
        if get_elevation(new_node) - get_elevation(node) > 1:
            continue
        visited.add(new_node)

        cost += 1
        heappush(heap, (cost, path_count + 1, new_node))

heap = []
visited = set()
heappush(heap, (0, 0, end))

while heap:
    cost, path_count, node = heappop(heap)

    if get_elevation(node) <= ord('a'):
        print("Part 2:", path_count)
        break

    for move in moves:
        new_node = (move[0] + node[0], move[1] + node[1])
        if new_node in visited:
            continue
        if not in_maze(new_node):
            continue
        if get_elevation(node) - get_elevation(new_node) > 1:
            continue
        visited.add(new_node)

        cost += 1
        heappush(heap, (cost, path_count + 1, new_node))
