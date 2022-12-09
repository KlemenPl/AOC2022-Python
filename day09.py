from shared import get_input

lines = get_input(9)

head = (0, 0)
prev_head = (0, 0)
tail = (0, 0)

visited = set()

for line in lines[:-1]:
    direction, amount = line.split()
    amount = int(amount)
    for step in range(amount):
        x = 0
        y = 0
        if direction == 'R':
            x = 1
        elif direction == 'L':
            x = -1
        elif direction == 'U':
            y = 1
        elif direction == 'D':
            y = -1

        prev_head = head[:]
        head = (head[0] + x, head[1] + y)
        dif_x = abs(tail[0] - head[0])
        dif_y = abs(tail[1] - head[1])
        dif = dif_x + dif_y
        is_ortho = dif_x == 0 or dif_y == 0
        if is_ortho and dif == 2:
            tail = prev_head
        elif not is_ortho and dif == 3:
            tail = prev_head
        visited.add(tail)

print("Part 1:", len(visited))

head = (0, 0)
tails = [(0, 0)] * 9
visited = set()

for line in lines[:-1]:
    direction, amount = line.split()
    amount = int(amount)
    for step in range(amount):
        x = 0
        y = 0
        if direction == 'R':
            x = 1
        elif direction == 'L':
            x = -1
        elif direction == 'U':
            y = 1
        elif direction == 'D':
            y = -1

        def simulate_tail(head, tail):
            dif_x = abs(head[0] - tail[0])
            dif_y = abs(head[1] - tail[1])

            if dif_x <= 1 and dif_y <= 1:
                return tail

            #print(tail)
            tail = list(tail)
            if head[0] - tail[0] > 0: tail[0] += 1  # go right
            elif head[0] - tail[0] < 0: tail[0] -= 1  # go left

            if head[1] - tail[1] > 0: tail[1] += 1  # go up
            elif head[1] - tail[1] < 0: tail[1] -= 1  # go down

            return tuple(tail)


        head = (head[0] + x, head[1] + y)
        tails[0] = simulate_tail(head, tails[0])
        for i in range(1, len(tails)):
            tails[i] = simulate_tail(tails[i - 1], tails[i])
        visited.add(tails[-1])

print("Part 2:", len(visited))



