from shared import get_input

lines = get_input(3)


def get_priority(c):
    if 'a' <= c <= 'z': return ord(c) - ord('a') + 1
    if 'A' <= c <= 'Z': return ord(c) - ord('A') + 27


total_priority = 0
for line in lines[:-1]:
    same = set(line[:len(line)//2]).intersection(set(line[len(line)//2:]))
    total_priority += get_priority(same.pop())

print("Part 1:", total_priority)
total_priority = 0

for a, b, c in zip(lines[::3], lines[1::3], lines[2::3]):
    same = set(a).intersection(b).intersection(c)
    if not same: continue
    total_priority += get_priority(same.pop())

print("Part 2:", total_priority)
