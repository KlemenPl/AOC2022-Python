import os
import requests


def get_input(day_num: int) -> list[str]:
    path = f"inputs/day_{day_num:02}"
    lines = list[str]
    if not os.path.exists(path):
        url = f"https://adventofcode.com/2022/day/{day_num}/input"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
        }
        with open('session.txt') as f:
            headers["Cookie"] = f"session={f.read()}"
        with requests.get(url, headers=headers) as response:
            data = response.text
            with open(path, "w") as f:
                f.write(data)

    with open(path) as f:
        lines = f.read().split('\n')
    return lines
