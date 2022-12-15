import time
from shared import get_input

lines = get_input(15)[:-1]

sensors = {}
for line in lines:
    parts = line.replace(',', '').replace(':', '').replace('=', ' ').split()
    sensor = (int(parts[3]), int(parts[5]))
    beacon = (int(parts[11]), int(parts[13]))
    sensors[sensor] = beacon

#LIMIT = 20
#SEARCH_Y = 10
LIMIT = 4000000
SEARCH_Y = 2000000


def dst(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_one():
    beacons_on_y = set()
    positions = set()
    for sensor, beacon in sensors.items():
        if beacon[1] == SEARCH_Y:
            beacons_on_y.add(beacon[0])

        dist = dst(sensor, beacon)
        dist -= abs(SEARCH_Y - sensor[1])

        positions.update(range(sensor[0] - dist, sensor[0] + dist + 1))
    return len(positions) - len(beacons_on_y)


def part_two():
    for y in range(0, LIMIT):
        positions = []
        for sensor, beacon in sensors.items():
            dist = dst(sensor, beacon)
            dist -= abs(y - sensor[1])

            from_range = max(0, sensor[0] - dist)
            to_range = min(LIMIT, sensor[0] + dist + 1)
            if from_range < to_range:
                positions.append((from_range, to_range))
        positions = sorted(positions, key=lambda x: x[0])
        to = positions[0][1]
        for pos in positions[1:]:
            if pos[0] > to:
                x = to
                return x * 4000000 + y
            to = max(to, pos[1])


start = time.time()
print("Part 1:", part_one())
end = time.time()
print("Took:", str(end - start), "s.\n")
start = time.time()
print("Part 1:", part_two())
end = time.time()
print("Took:", str(end - start), "s.")
