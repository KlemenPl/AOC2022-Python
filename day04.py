from shared import get_input

lines = get_input(4)


def is_fully_contained(a, b):
    a_min, a_max = a.split("-")
    b_min, b_max = b.split("-")
    a_min = int(a_min)
    a_max = int(a_max)
    b_min = int(b_min)
    b_max = int(b_max)
    return a_min >= b_min and a_max <= b_max


count = 0
for line in lines[:-1]:
    a, b = line.split(",")
    if is_fully_contained(a, b) or is_fully_contained(b, a):
        count += 1

print("Part 1:", count)
count = 0


def create_range(min_val, max_val):
    min_val = int(min_val)
    max_val = int(max_val)
    return range(min_val, max_val + 1)


for line in lines[:-1]:

    a, b = line.split(",")
    a = create_range(*a.split("-"))
    b = create_range(*b.split("-"))

    overlap = set(a) & set(b)
    if overlap:
        count += 1

print("Part 2:", count)
