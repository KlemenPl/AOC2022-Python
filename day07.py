from shared import get_input
from collections import defaultdict

lines = get_input(7)[1:]

folder_files = defaultdict(list)
folder_sizes = {}
i = 0
path = []
# First pass: map out folder contents
while i < len(lines):
    parts = lines[i].split()
    if lines[i] == "$ cd ..":
        path.pop()
    elif lines[i].startswith("$ cd"):
        path.append(parts[2])
    elif lines[i].startswith("$ ls"):
        i += 1
        while not lines[i].startswith("$") and lines[i]:
            size, name = lines[i].split()
            folder_files['/'.join(path)].append((size, name))
            i += 1
        i -= 1
    i += 1

# Second pass: map out folder sizes
i = 0
path = []


def get_foler_size(curr_path):
    sum_size = 0
    for file_size, file in folder_files[curr_path]:
        if file_size == "dir":
            file_size = get_foler_size(f"{curr_path}/{file}".lstrip("/"))
        sum_size += int(file_size)
    folder_sizes[curr_path] = sum_size
    return sum_size


get_foler_size("")
print(folder_files)
# Part 1
sum_size = 0
for size in folder_sizes.values():
    if size < 100000:
        sum_size += size

print("Part 1:", sum_size)

# Part 2

used_space = folder_sizes[""]
available_space = 70000000 - used_space
needed_space = max(0, 30000000 - available_space)

sizes = folder_sizes.values()
sizes = [x for x in sizes if x >= needed_space]
print("Part 2:", min(sizes))

