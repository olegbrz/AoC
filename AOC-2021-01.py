from typing import List
from aoc_helper import get_input

input_ = list(map(int, get_input()))


def sonar_sweep(data: List[int], w_size: int = 1) -> int:
    wind = [sum(data[i-w_size+1:i+1])
            for i in range(w_size-1, len(data))]
    incr = [wind[j] > wind[j-1]
            for j in range(1, len(wind))]
    return incr.count(True)


print(f"Part 1: {sonar_sweep(input_)}")
print(f"Part 2: {sonar_sweep(input_, 3)}")
