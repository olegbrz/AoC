from typing import List
from aoc_helper import get_input, benchmark
from string import ascii_letters

input_ = get_input()


priority = {letter: i + 1 for i, letter in enumerate(ascii_letters)}


@benchmark
def get_errors(data: List[str]) -> int:
    prty_sum = 0
    for rucksack in data:
        half = len(rucksack) // 2
        half1, half2 = rucksack[:half], rucksack[half:]
        common = list(set(half1).intersection(set(half2)))[0]
        prty_sum += priority[common]
    return prty_sum


@benchmark
def get_badges(data: List[str]) -> int:
    prty_sum = 0
    for i in range(0, len(data), 3):
        g1, g2, g3 = set(data[i]), set(data[i + 1]), set(data[i + 2])
        common = list(g1.intersection(g2).intersection(g3))[0]
        prty_sum += priority[common]
    return prty_sum


print(f"Part 1: {get_errors(input_)}")
print(f"Part 2: {get_badges(input_)}")
