from requests.api import get
from aoc_helper import get_input, benchmark
from itertools import cycle

input_ = get_input()


@benchmark
def chronal_calibration(data, twice=False):
    if twice:
        data = cycle(data)
    frequencies = [0]
    freq = 0
    for change in data:
        freq += int(change)
        if freq not in frequencies:
            frequencies.append(freq)
        elif twice:
            return freq
    return freq


print(f"Part 1: {chronal_calibration(input_)}")
print(f"Part 2: {chronal_calibration(input_, twice=True)}")
