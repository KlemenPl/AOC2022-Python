from shared import get_input
from functools import cmp_to_key

lines = get_input(13)


def cmp(lhs: int, rhs: int) -> int:
    if lhs < rhs:
        return -1
    if lhs > rhs:
        return 1
    else:
        return 0


def is_in_right_order(left, right):
    if type(left) is int and type(right) is int:
        return cmp(left, right)
    if type(left) is list and type(right) is list:
        for l, r in zip(left, right):
            is_right = is_in_right_order(l, r)
            if is_right != 0:
                return is_right
        return cmp(len(left), len(right))
    else:
        if type(left) is int:
            left = [left]
        elif type(right) is int:
            right = [right]
        return is_in_right_order(left, right)


sum_indices = 0
for i in range(0, len(lines) - 1, 3):
    left = eval(lines[i])
    right = eval(lines[i + 1])
    if is_in_right_order(left, right) == -1:
        sum_indices += i // 3 + 1

print("Part 1:", sum_indices)

div1 = [[2]]
div2 = [[6]]
packets = [div1, div2]
for i in range(0, len(lines) - 1, 3):
    left = eval(lines[i])
    right = eval(lines[i + 1])
    packets.append(left)
    packets.append(right)

packets = sorted(packets, key=cmp_to_key(is_in_right_order))
div1 = packets.index(div1) + 1
div2 = packets.index(div2) + 1
print("Part 2:", div1 * div2)

