from shared import get_input

lines = get_input(2)

total_score = 0

ROCK = 0
PAPER = 1
SCISSORS = 2

for line in lines:
    if not line:
        continue
    opponent, response = line.split()
    opponent = ord(opponent[0]) - ord('A')
    response = ord(response[0]) - ord('X')
    total_score += response + 1

    if response == ROCK and opponent == SCISSORS or \
            response == PAPER and opponent == ROCK or \
            response == SCISSORS and opponent == PAPER:
        total_score += 6

    if response == opponent:
        total_score += 3

print("Part 1:", total_score)
total_score = 0

for line in lines:
    if not line:
        continue
    opponent, response = line.split()
    opponent = ord(opponent[0]) - ord('A')

    win = 0
    draw = opponent
    lose = 0

    if opponent == ROCK:
        win = PAPER
        lose = SCISSORS
    elif opponent == PAPER:
        win = SCISSORS
        lose = ROCK
    else:
        win = ROCK
        lose = PAPER

    if response == "X": total_score += lose + 1
    if response == "Y": total_score += 3 + draw + 1
    if response == "Z": total_score += 6 + win + 1

print("Part 2:", total_score)
