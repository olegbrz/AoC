#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from aoc_helper import get_input, benchmark
from statistics import mean, stdev


def fuel(pos_i: int, pos_f: int) -> int: return abs(pos_f-pos_i)


def crab_fuel(pos_i: int, pos_f: int) -> int:
    return int((1 + abs(pos_i - pos_f)) * abs(pos_i - pos_f) / 2)


@benchmark
def optimal_align(positions: List[int], crab_eng: bool = False) -> int:
    best_result = float('inf')
    x, bracketing = int(mean(positions)), int(stdev(positions) / 3)
    search_range = range(x-bracketing, x+bracketing)
    for i in search_range:
        fuel_func = crab_fuel if crab_eng else fuel
        req_fuel = sum([fuel_func(p, i) for p in positions])
        if req_fuel < best_result:
            best_result = req_fuel
    return best_result


input_ = list(map(int, get_input(as_string=True).split(',')))

print(f"Part 1: {optimal_align(input_)}")
print(f"Part 2: {optimal_align(input_, crab_eng=True)}")
