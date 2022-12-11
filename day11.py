import math

from shared import get_input


class Monkey:
    def __init__(self, items, op, op_lhs, op_rhs, test_div, if_true, if_false):
        self.items = items
        self.op = op
        self.op_lhs = op_lhs
        self.op_rhs = op_rhs
        self.test_div = test_div
        self.if_true = if_true
        self.if_false = if_false


lines = get_input(11)

def parse_input():
    monkeys = []
    idx = 0
    while idx < len(lines):
        if not lines[idx].startswith("Monkey "):
            idx += 1
            continue
        items = lines[idx + 1]
        op = lines[idx + 2]
        test = lines[idx + 3]
        if_true = lines[idx + 4]
        if_false = lines[idx + 5]

        items = items[items.index(':') + 1:].split(',')
        items = [int(x) for x in items]

        op = op.split()
        op_lhs = op[-3]
        op_rhs = op[-1]
        op = op[-2]

        test = int(test.split()[-1])
        if_true = int(if_true.split()[-1])
        if_false = int(if_false.split()[-1])

        idx += 6
        monkey = Monkey(items, op, op_lhs, op_rhs, test, if_true, if_false)
        monkeys.append(monkey)
    return monkeys


def simulate_round(monkeys, div_worry, mul_worry):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            num_inspected[i] += 1
            item = monkey.items.pop(0)
            worry = item
            op_lhs = monkey.op_lhs
            op_rhs = monkey.op_rhs
            op_lhs = int(worry) if op_lhs == 'old' else int(op_lhs)
            op_rhs = int(worry) if op_rhs == 'old' else int(op_rhs)
            if monkey.op == '*':
                worry = op_lhs * op_rhs
            elif monkey.op == '+':
                worry = op_lhs + op_rhs
            if div_worry > 0:
                worry //= div_worry
            if mul_worry:
                worry %= mul_worry

            throw_to = monkey.if_true if worry % monkey.test_div == 0 else monkey.if_false
            monkeys[throw_to].items.append(worry)


monkeys = parse_input()
num_inspected = [0] * len(monkeys)

for i in range(20):
    simulate_round(monkeys, 3, 0)

num_inspected_s = sorted(num_inspected)
print("Part 1:", num_inspected_s[-1] * num_inspected_s[-2])

monkeys = parse_input()
num_inspected = [0] * len(monkeys)

# Find LCM
all_divisors = []
for monkey in monkeys:
    all_divisors.append(monkey.test_div)

divisor = math.lcm(*all_divisors)
print("Divisor:", divisor)
for i in range(10000):
    simulate_round(monkeys, 0, divisor)

num_inspected_s = sorted(num_inspected)
print("Part 2:", num_inspected_s[-1] * num_inspected_s[-2])
