from shared import get_input

lines = get_input(6)

signal = lines[0]


def find_marker(stride):
    for i in range(stride, len(signal), 1):
        packet = signal[i - stride:i]
        if len(set(packet)) == len(packet):
            # print(packet)
            return i
    return None


print("Part 1:", find_marker(4))
print("Part 2:", find_marker(14))
