#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import get_input, benchmark


def req_fuel(x): return x // 3 - 2


def rocket_eq(mass):
    return req_fuel(mass) + rocket_eq(req_fuel(mass)) if mass >= 9 else 0


@benchmark
def compute_fuel(module_masses, include_fuel=False):
    map_func = rocket_eq if include_fuel else req_fuel
    return sum(map(map_func, module_masses))


input_ = list(map(int, get_input()))

print(f"Part 1: {compute_fuel(input_)}")
print(f"Part 2: {compute_fuel(input_, include_fuel=True)}")
