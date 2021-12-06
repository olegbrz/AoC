#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from aoc_helper import get_input, benchmark


@benchmark
def get_population(initial: List[int], days: int) -> int:
    fish = [initial.count(i) for i in range(8, -1, -1)]
    for _ in range(days):
        fish.insert(0, fish[8])
        fish[2] += fish.pop(9)
    return sum(fish)


input_ = list(map(int, get_input(as_string=True)[:-1].split(',')))

print(f"Part 1: {get_population(input_, 80)}")
print(f"Part 2: {get_population(input_, 256)}")
