from shared import get_input
from heapq import *
import time as t


lines = get_input(16)[:-1]

valves = {}
non_zero_valves = set()

for line in lines:
    line = line.replace('=', ' ').replace(';', '').replace(',', '')
    parts = line.split()

    #print(line)
    valve = parts[1]
    flow_rate = int(parts[5])
    connected = parts[parts.index('to') + 2:]
    valves[valve] = (flow_rate, connected)
    if flow_rate:
        non_zero_valves.add(valve)


def get_max_flow_rate(time_remaining, visited):
    not_visited = non_zero_valves - visited
    sum_rate = sum(valves[x][0] for x in not_visited)
    return sum_rate * time_remaining


best_cost = 0


def part_one():
    MAX = sum([x[0] for _, x in valves.items()]) * 30

    # current_flow_rate, time_remaining, max_remaining_flow_rate, pos, visited
    start = (MAX, 0, 26, "AA", {"AA"})
    q = [start]

    while q:
        p, flow_rate, time, curr, visited = heappop(q)
        if time == 0:
            return flow_rate

        if curr not in visited and valves[curr][0] > 0:
            new_visited = visited | {curr}
            rate = (valves[curr][0] * (time - 1))
            heappush(q, (MAX - flow_rate - rate - get_max_flow_rate(time - 1, new_visited), flow_rate + rate, time - 1, curr, new_visited))
        # Visit neighbours
        for node in valves[curr][1]:
            if node in visited:
                continue
            new_visited = visited | {curr}
            heappush(q, (MAX - flow_rate - get_max_flow_rate(time - 1, new_visited), flow_rate, time - 1, node, new_visited))


def part_two():
    # TODO
    pass



start = t.time()
print("Part 1:", part_one())
end = t.time()
print("Took:", str(end - start), "s.\n")

start = t.time()
print("Part 2:", part_two())
end = t.time()
print("Took:", str(end - start), "s.\n")