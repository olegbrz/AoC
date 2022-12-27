#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aoc_helper import *
import numpy as np


@parsing_benchmark
def parse_input(data):
    return data


@benchmark
def compute(instructions):
    is_20mod40 = lambda x: (x - 20) % 40 == 0
    accum, cycle = 0, 0
    reg = 1
    for instr in instructions:
        cycle += 1
        if is_20mod40(cycle):
            accum += reg * cycle
        if instr[0] == "a":
            cycle += 1
            amount = int(instr.split()[1])
            if is_20mod40(cycle):
                accum += reg * cycle
            reg += amount
    return accum


@benchmark
def emulate_crt(instructions):
    pixel_state = lambda c, X: 1 if (c - 1) % 40 in [X - 1, X, X + 1] else 0
    crt_position = lambda c: ((c - 1) // 40, (c - 1) % 40)
    crt = np.zeros((6, 40), dtype=bool)
    reg = 1
    cycle = 0

    for instr in instructions:
        cycle += 1
        crt[crt_position(cycle)] = pixel_state(cycle, reg)
        if instr[0] == "a":
            cycle += 1
            amount = int(instr.split()[1])
            crt[crt_position(cycle)] = pixel_state(cycle, reg)
            reg += amount

    crt_str = "\n"
    for row in crt:
        crt_str += "".join("█" if x else " " for x in row) + "\n"

    return crt_str


data = parse_input(get_input())

print(f"Part 1: {compute(data)}")
print(f"Part 2: {emulate_crt(data)}")
