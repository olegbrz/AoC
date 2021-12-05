#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from typing import List, Literal
from aoc_helper import benchmark, get_input


def transform_input(x: str) -> List[int]:
    return list(map(int, x.replace(" -> ", ",").split(",")))


def is_linear(x: List[int]) -> bool:
    return x[0] == x[2] or x[1] == x[3]


def coords_to_seq(c: List[int], axis: Literal["x", "y"]) -> List[int]:
    i = [0, 2] if axis == "x" else [1, 3]
    start = c[i[0]]
    target = c[i[1]] + (1 if c[i[1]] >= c[i[0]] else -1)
    step = 1 if c[i[0]] <= c[i[1]] else -1
    return list(range(start, target, step))


@benchmark
def hydrothermal_overlaps(data: List[str], diagonals: bool = False) -> int:
    coords = list(map(transform_input, data))
    if not diagonals:
        coords = np.array(list((filter(is_linear, coords))))

    dim = np.max(coords) + 1
    diagram = np.zeros([dim, dim])

    for c in coords:
        seq_x, seq_y = coords_to_seq(c, "x"), coords_to_seq(c, "y")
        if len(seq_y) == 1:
            seq_y *= len(seq_x)
        elif len(seq_x) == 1:
            seq_x *= len(seq_y)
        for x, y in zip(seq_x, seq_y):
            diagram[y, x] += 1
    return np.count_nonzero(diagram > 1)


input_ = get_input()

print(f"Part 1: {hydrothermal_overlaps(input_)}")
print(f"Part 2: {hydrothermal_overlaps(input_, diagonals=True)}")
