from typing import List
from aoc_helper import get_input

input_ = get_input()


def sqft_of_wrap(data: List[str]) -> int:
    wrap_sqft = 0
    for p in data:
        l, w, h = map(int, p.split("x"))
        wrap_sqft += (2 * l * w + 2 * w * h + 2 * h * l)
        wrap_sqft += min([l*w, w*h, h*l])
    return wrap_sqft


def ft_of_ribbon(data: List[str]) -> int:
    ribbon_ft = 0
    for p in data:
        l, w, h = map(int, p.split("x"))
        shortest_side1, shortest_side2 = sorted([l, w, h])[:2]
        lowest_perim = 2 * (shortest_side1 + shortest_side2)
        ribbon_ft += (lowest_perim + l * w * h)
    return ribbon_ft


print(f"Part 1: {sqft_of_wrap(input_)}")
print(f"Part 2: {ft_of_ribbon(input_)}")
