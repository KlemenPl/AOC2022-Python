from shared import get_input

lines = get_input(1)
lines.append('')

num_cals = []
cur_sum = 0

for line in lines:
    if line:
        cur_sum += int(line)
    else:
        num_cals.append(cur_sum)
        cur_sum = 0

num_cals.sort(reverse=True)
print(num_cals[:3])
print(sum(num_cals[:3]))
